from pycollatex import *
from time import perf_counter
from pathlib import Path

collation = Collation()
collation.add_plain_witness("A", Path("data/t1_W1_unicode.txt").read_text())
collation.add_plain_witness("B", Path("data/t1_W2_unicode.txt").read_text())

t1_start = perf_counter()

collation_graph = collate(collation, segmentation=False)

t1_stop = perf_counter()

# before refactoring: 1037s, now 17s

print("time in Unicode: %f", t1_stop-t1_start)

collation = Collation()
collation.add_plain_witness("A", Path("data/t1_W1_wylie.txt").read_text())
collation.add_plain_witness("B", Path("data/t1_W2_wylie.txt").read_text())

t1_start = perf_counter()

collation_graph = collate(collation, segmentation=False)

t1_stop = perf_counter()

# before refactoring: 65s, now 91s

print("time in EWTS: %f", t1_stop-t1_start)

#alignment_table = output_collation_graph(collation, collation_graph)
#print(alignment_table)