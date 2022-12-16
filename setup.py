import re
from pathlib import Path
from setuptools import find_packages, setup

def read(fname):
    p = Path(__file__).parent / fname
    with p.open(encoding="utf-8") as f:
        return f.read()

def get_version(prop, project):
    project = Path(__file__).parent / project / "__init__.py"
    result = re.search(
        r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), project.read_text()
    )
    return result.group(1)

setup(
    name='pycollatex',
    version=get_version("__version__", "pycollatex"),
    description='Fork of the CollateX collation tool',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author='Ronald Haentjens Dekker, then the OpenPecha development team',
    url='https://github.com/OpenPecha/pycollatex',
    packages=find_packages(),
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
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    python_requires=">=3.7",
)