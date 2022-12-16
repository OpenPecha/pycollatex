# PyCollateX

PyCollateX is a fork of [CollateX-pythonport](https://github.com/interedition/collatex/tree/master/collatex-pythonport) with:
- improvements for Python3 and Unicode regex
- less dependencies (at the cost of export features)

CollateX is a software to

- read multiple (>= 2) versions of a text, splitting each version into parts (tokens) to be compared,
- identify similarities of and differences between the versions (including moved/transposed segments) by aligning tokens, and
- output the alignment results in a variety of formats for further processing, for instance to support the production of a critical apparatus or the stemmatic analysis of a text's genesis.

### Features

* Partially non-progressive multiple-sequence alignment
* Multiple output formats: alignment table, variant graph
* Near matching (optional)

### Simple example

```python
from pycollatex import *

collation = Collation()
collation.add_plain_witness("A", "The quick brown fox jumps over the dog.")
collation.add_plain_witness("B", "The brown fox jumps over the lazy dog.")

alignment_table = collate(collation)
print(alignment_table)
```

outputs:

```
+---+-----+-------+--------------------------+------+------+
| A | The | quick | brown fox jumps over the | -    | dog. |
| B | The | -     | brown fox jumps over the | lazy | dog. |
+---+-----+-------+--------------------------+------+------+
```

### Original CollateX Contributors

##### Authors
* Ronald Haentjens Dekker
* Gregor Middell

##### Contributors
* David J. Birnbaum (for Windows support and installation documentation)
* Tara L. Andrews (for bugfixes and patches)