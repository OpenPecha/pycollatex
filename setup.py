from setuptools import find_packages, setup

readme = open('README.md').read()

setup(
    name='pycollatex',
    version='3.0',
    description='CollateX is a collation tool.',
    long_description=readme,
    author='Ronald Haentjens Dekker, then OpenPecha development team',
    author_email='info@bdrc.io',
    url='https://github.com/OpenPecha/pycollatex',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'networkx',
        'prettytable',
        'levenshtein',
        'regex'
    ],
    license="GPLv3",
    keywords='CollateX',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English'
    ],
    test_suite='tests',
    python_requires=">=3.7",
)