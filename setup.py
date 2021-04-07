from setuptools import setup


setup(
    name='cldfbench_nen',
    py_modules=['cldfbench_nen'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'nen=cldfbench_nen:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'pydictionaria>=2.0',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
