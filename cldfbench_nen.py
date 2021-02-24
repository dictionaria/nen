from collections import ChainMap
import pathlib

from pydictionaria.sfm_lib import Database as SFM
from pydictionaria.preprocess_lib import (
    marker_fallback_sense, marker_fallback_entry
)
from pydictionaria import sfm2cldf

from cldfbench import CLDFSpec, Dataset as BaseDataset


def reorganize(sfm):
    return sfm


def preprocess(entry):
    entry = marker_fallback_entry(entry, 'lx', 'lx_Nen')
    entry = marker_fallback_entry(entry, 'lx', 'lc')
    entry = marker_fallback_sense(entry, 'de', 'ge')
    return entry


# Postprocessing

def authors_string(authors):
    def is_primary(a):
        return not isinstance(a, dict) or a.get('primary', True)

    primary = ' and '.join(
        a['name'] if isinstance(a, dict) else a
        for a in authors
        if is_primary(a))
    secondary = ' and '.join(
        a['name']
        for a in authors
        if not is_primary(a))
    if primary and secondary:
        return '{} with {}'.format(primary, secondary)
    else:
        return primary or secondary


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "nen"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(
            dir=self.cldf_dir,
            module='Dictionary',
            metadata_fname='cldf-metadata.json')

    def cmd_download(self, args):
        """
        Download files to the raw/ directory. You can use helpers methods of `self.raw_dir`, e.g.

        >>> self.raw_dir.download(url, fname)
        """
        pass

    def cmd_makecldf(self, args):
        """
        Convert the raw data to a CLDF dataset.

        >>> args.writer.objects['LanguageTable'].append(...)
        """

        # read data

        md = self.etc_dir.read_json('md.json')
        properties = md.get('properties') or {}
        language_name = md['language']['name']
        isocode = md['language']['isocode']
        language_id = md['language']['isocode']
        glottocode = md['language']['glottocode']

        marker_map = ChainMap(
            properties.get('marker_map') or {},
            sfm2cldf.DEFAULT_MARKER_MAP)
        entry_sep = properties.get('entry_sep') or sfm2cldf.DEFAULT_ENTRY_SEP
        sfm = SFM(
            self.raw_dir / 'db.sfm',
            marker_map=marker_map,
            entry_sep=entry_sep)

        examples = sfm2cldf.load_examples(self.raw_dir / 'examples.sfm')

        if (self.etc_dir / 'cdstar.json').exists():
            media_catalog = self.etc_dir.read_json('cdstar.json')
        else:
            media_catalog = {}

        # preprocessing

        sfm = reorganize(sfm)
        sfm.visit(preprocess)

        # processing

        with open(self.dir / 'cldf.log', 'w', encoding='utf-8') as log_file:
            log_name = '%s.cldf' % language_id
            cldf_log = sfm2cldf.make_log(log_name, log_file)

            entries, senses, examples, media = sfm2cldf.process_dataset(
                self.id, language_id, properties,
                sfm, examples, media_catalog=media_catalog,
                glosses_path=self.raw_dir / 'glosses.flextext',
                examples_log_path=self.dir / 'examples.log',
                glosses_log_path=self.dir / 'glosses.log',
                cldf_log=cldf_log)

            # good place for some post-processing

            # cldf schema

            sfm2cldf.make_cldf_schema(
                args.writer.cldf, properties,
                entries, senses, examples, media)

            sfm2cldf.attach_column_titles(args.writer.cldf, properties)

            print(file=log_file)

            entries = sfm2cldf.ensure_required_columns(
                args.writer.cldf, 'EntryTable', entries, cldf_log)
            senses = sfm2cldf.ensure_required_columns(
                args.writer.cldf, 'SenseTable', senses, cldf_log)
            examples = sfm2cldf.ensure_required_columns(
                args.writer.cldf, 'ExampleTable', examples, cldf_log)
            media = sfm2cldf.ensure_required_columns(
                args.writer.cldf, 'media.csv', media, cldf_log)

            entries = sfm2cldf.remove_senseless_entries(
                senses, entries, cldf_log)

        # output

        args.writer.cldf.properties['dc:creator'] = authors_string(
            md.get('authors') or ())

        language = {
            'ID': language_id,
            'Name': language_name,
            'ISO639P3code': isocode,
            'Glottocode': glottocode,
        }
        args.writer.objects['LanguageTable'] = [language]

        args.writer.objects['EntryTable'] = entries
        args.writer.objects['SenseTable'] = senses
        args.writer.objects['ExampleTable'] = examples
        args.writer.objects['media.csv'] = media
