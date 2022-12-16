### Normalization
- configurable normalization function

### Matching
- Near matching as a post process (in experimental branch of David's fork)

### Transposition detection
- TODO: there is no transposition detection
- Find match phrases: NOT YET NEEDED, optional
- Find transpositions: NOT YET NEEDED, optional
- Merge transpositions into graph: TODO
- Optimization:	a* search algorithm as optimization: NOT YET NEEDED

### Special cases
- failing use case in test_collatex_block_witnesses.py, name: test_blocks_failing_transposition_use_case_old_algorithm
- Blocks should not start with punctuation
- Scoring should take length of blocks into account