# Change log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/). It follows [some conventions](http://keepachangelog.com/).

## [3.0.0] - Unreleased
### Fixed
- fixes for Python3
- update dependencies

### Changed
- rename to `pycollatex`
- use of the regex library to improve tokenization for non-Latin scripts
- merge following tshegs (U+0F02, U+0F03, U+0FD2) into token (like space is)
- reduce output options to reduce the code base

## [2.2] - 20180816
* Create documentation for CollateX Python
* TEI output writes "t" values instead of "n" values
* TEI output uses minidom instead of etree
* TEI output uses same namespaces and wrapper as CollateX Java
* Add "csv" and "tsv" output options
* Use graphviz Python bindings instead of PyGraphviz for Windows compatibility

## [2.1.3rc2] - 20180810
* Update networkx compatibility from 1.11 to 2.1
* Replace pygraphviz bindings with graphviz for Windows compatibility
* Update near matching to add near-matching edges and adjust rank in SVG output

## [2.1.3rc1] - 20171009
* New version of the alignment algorithm (which we call the MatchCube approach)
  to reduce order effects during multiple witness alignment.

## [2.1.3rc0] - 20170724
* Added the new SVG renderer which uses the pygraphviz bindings instead of the graphviz bindings.
* Thanks to David J. Birnbaum for the patch.
* Fixed the CalledProcessError bug that the previous renderer caused when used with Python 3.

## [2.1.2] - 20170110
* Added the ability to use output="svg_simple" next to output="svg". The "svg_simple" option gets you the n-property
* based graph, so just the normalized version of the tokens, which will hide any variation in the t-property.
* Thanks to Joris van Zundert for the patch.
* Changed the colour scheme of the "html2" output option, to aid those with Red/Green colour-blindness.
* Thanks to Melodee H. Beals for the patch.

## [2.1.1] - 20161217
* Bug fix release
* Fixed a bug in the new near match functionality that would cause tokens to go missing in the alignment table.
* Thanks to Torsten Hiltmann for reporting it and providing a test case.

## [2.1.0] - 20161101
* Official release for the Dixit code and collation workshop in Amsterdam
* This release contains the new near match functionality implemented as a post process after alignment. Same as RC1.
* It also contains the multiple short witnesses bugfix done in 2.0.1


## [2.0.1] - 20161030
* Bug fix release for the Dixit code and collation workshop in Amsterdam
* Fixed index out of range bug when multiple very short witnesses (= one token) were collated
* Disabled debug statements for near matching

## [2.1.0rc1] - 20161016
* New near match functionality, implemented as a post process after alignment.

## [2.0.0] - 20161015
* First official release for the Dixit code and collation workshop in Amsterdam
* Added XML as an output format
* Added TEI parallel segmentation as an output format
* Tokenizer: retain whitespace in the t-property of preceding token
* Witness: added normalization: strips whitespace

## [2.0.0rc20] - 20160718
* Merged old collate_pretokenized_json() function into collate() function
* JSON output contains full JSON representation of the tokens
* Enabled segmentation support for all input formats, and for SVG output
* Enhanced SVG output to include "n" value and all "t" values of JSON input
* JSON output is raw Unicode, instead of escaped characters
* Test suite updated

## [2.0.0rc19] - 20151210
* Rename of TokenIndex.py was not in effect in the uploaded files. Fixed now.

## [2.0.0rc18] - 20151125
* Renamed TokenIndex.py module to tokenindex.py to follow conventions.

## [2.0.0rc17] - 20151125
* Moved all the block and suffix, LCP interval code to new class TokenIndex.

## [2.0.0rc16] - 20150628
* Added output option 'html2' for colored alignment table rendering.

## [2.0.0rc15] - 20150628
* Fix a bug that was caused by the fact that a dash was stored in empty cells of the AlignmentTable. Now None is stored (this resolved a TODO). Plain text and HTML rendering of the table render a dash for empty cells. JSON output now returns null for empty cells. Fixes bug when a token with a dash in the content was screwing the rendering of the alignment table (caused of by one errors).

## [2.0.0rc14] - 20150627
* Further improved blockification of witnesses.

## [2.0.0rc13] - 20150621
* Added properties_filter option to enable users to influence matching based on properties of tokens.
* Improved blockification of witnesses.

## [2.0.0pre12] - 20150512
* Added SVG output option to the collate function. For this functionality to work the graphviz python library needs to be installed.

## [2.0.0pre11] - 20141202
* Bug-fix: collate_pretokenize_json function should not re-tokenized the content. Thanks to Tara L. Andrews.
* Allow near-matching for plain as well as for pre-tokenized content. Thanks to Tara L. Andrews.
* Added HTML option to collate function for the output as an alignment table represented as HTML.

## [2.0.0pre10] - 20141113
* Added support for Unicode character encoding
* Ported codebase from Python 2 to Python 3
* Separated IPython display logic from functional logic. No longer will the collate function try to determine whether you are running an environment that is capable of display HTML or SVG.

## [2.0.0pre9] - 20141002
* Added near matching option to collate function.
* Added variant or invariant status to columns in alignment table object and JSON output.
* Added experimental A* decision graph search optimization.

## [2.0.0pre8] - 20140918
* Added WordPunctuationTokenizer (treats punctuation as separate tokens).
* Combined suffix array and edit graph aligner approaches into one collation algorithm.

## [2.0.0pre7] - 20140714
* Fixed handling of segmentation parameter in pretokenized JSON function.

## [2.0.0pre6] - 20140630
* Added Windows support. Thanks to David J. Birnbaum.
* Fixed handling of IPython imports.

## [2.0.0pre5] - 20140611
* Added JSON output to collate method.
* Added option to collate method to enable or disable parallel segmentation.
* Added table output to collate_pretokenized_json method, next to the already existing JSON output.
* Cached the suffix and LCP arrays to prevent unnecessary recalculation
* Fixed handling of empty cells in JSON output of pretokenized JSON.
* Fixed compatibility issue when rendering HTML or SVG with IPython 2.1 instead of IPython 0.13.
* Corrected RST syntax in package info description.

## [2.0.0pre4] - 20140611
* Added pretokenized JSON support.
* Added JSON visualization for the alignment table.

## [2.0.0pre3] - 20140610
* Fixed imports in init.py, "from collatex import \*" now works correctly.
* Added IPython HTML support for alignment table.
* Added IPython SVG support for variant graph.
* Added convenience constructors on Collation object.
* Added horizontal layout for the alignment table visualization, next to vertical one.

## [2.0.0pre2] - 20140609
* Removed max 6 witness limit in aligner, now n number of witnesses can be aligned.
* Added transposition detection.
* Added alignment table plus plain text visualization.
* Added collate convenience function.

## [2.0.0pre1] - 20140602
* First release on PyPI.
* First pure Python development release of CollateX.
* New collation algorithm, which does non progressive multiple witness alignment.