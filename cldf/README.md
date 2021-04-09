<a name="ds-cldfmetadatajson"> </a>

# Dictionary Nen Dictionary

**CLDF Metadata**: [cldf-metadata.json](./cldf-metadata.json)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Evans, Nicholas. 2019. Nen dictionary. Dictionaria 8. 1-5005 (Available online at https://dictionaria.clld.org/contributions/nen)
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Dictionary](http://cldf.clld.org/v1.0/terms.rdf#Dictionary)
[dc:creator](http://purl.org/dc/terms/creator) | Nicholas Evans
[dc:identifier](http://purl.org/dc/terms/identifier) | https://dictionaria.clld.org/contributions/nen
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/dictionaria/nen
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/dictionaria/nen/tree/9818ddc">dictionaria/nen v1.1-12-g9818ddc</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.3">Glottolog v4.3</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.5</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | nen
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-entriescsv"></a>Table [entries.csv](./entries.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF EntryTable](http://cldf.clld.org/v1.0/terms.rdf#EntryTable)
[dc:extent](http://purl.org/dc/terms/extent) | 5005


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Headword](http://cldf.clld.org/v1.0/terms.rdf#headword) | `string` | 
[Part_Of_Speech](http://cldf.clld.org/v1.0/terms.rdf#partOfSpeech) | `string` | 
`Citation_Form` | `string` | 
`Codiathetic` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Dual_NonDual_Pair` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Entry_IDs` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Etymology` | `string` | 
`Etymology_Nen` | `string` | 
`General_Comment` | `string` | 
`Grammar_Comment` | `string` | 
`Main_Entry` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Meaning_Origin_Word` | `string` | 
`Media_IDs` | list of `string` (separated by ` ; `) | References [media.csv::ID](#table-mediacsv)
`Minimal_Pair` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Variant_Form` | `string` | 

## <a name="table-sensescsv"></a>Table [senses.csv](./senses.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF SenseTable](http://cldf.clld.org/v1.0/terms.rdf#SenseTable)
[dc:extent](http://purl.org/dc/terms/extent) | 5972


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Entry_ID](http://cldf.clld.org/v1.0/terms.rdf#entryReference) | `string` | References [entries.csv::ID](#table-entriescsv)
`Antonym` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Encyclopedic_Info` | `string` | 
`Media_IDs` | list of `string` (separated by ` ; `) | References [media.csv::ID](#table-mediacsv)
`Near_Synonym` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Scientific_Name` | `string` | 
`Semantic_Domain` | `string` | 
`Synonym` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)

## <a name="table-examplescsv"></a>Table [examples.csv](./examples.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable)
[dc:extent](http://purl.org/dc/terms/extent) | 5103


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | 
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `\t`) | 
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `\t`) | 
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | 
[Meta_Language_ID](http://cldf.clld.org/v1.0/terms.rdf#metaLanguageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Sense_IDs` | list of `string` (separated by ` ; `) | References [senses.csv::ID](#table-sensescsv)

## <a name="table-mediacsv"></a>Table [media.csv](./media.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 229


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
`Filename` | `string` | 
`URL` | `anyURI` | 
`mimetype` | `string` | 
`size` | `integer` | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 1


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 

