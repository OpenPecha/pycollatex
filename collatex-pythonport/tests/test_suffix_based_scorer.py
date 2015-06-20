import unittest
from ClusterShell.RangeSet import RangeSet
from collatex import Collation
from collatex.collatex_suffix import Block
from collatex.suffix_based_scorer import Scorer

__author__ = 'ronalddekker'


class Test(unittest.TestCase):

    def test_non_overlapping_blocks_Hermans(self):
        collation = Collation()
        collation.add_plain_witness("W1", "a b c d F g h i ! K ! q r s t")
        collation.add_plain_witness("W2", "a b c d F g h i ! q r s t")
        algorithm = Scorer(collation)
        blocks = algorithm._get_non_overlapping_repeating_blocks()
        self.assertIn(Block(RangeSet("0-8, 17-25")), blocks) # a b c d F g h i !
        self.assertIn(Block(RangeSet("11-14, 26-29")), blocks) # q r s t


    def test_blocks_Hermans_case_three_witnesses(self):
        collation = Collation()
        collation.add_plain_witness("W1", "a b c d F g h i ! K ! q r s t")
        collation.add_plain_witness("W2", "a b c d F g h i ! q r s t")
        collation.add_plain_witness("W3", "a b c d E g h i ! q r s t")
        algorithm = Scorer(collation)
        blocks = algorithm._get_non_overlapping_repeating_blocks()
        self.assertIn(Block(RangeSet("0-3, 17-20, 32-35")), blocks) # a b c d
        self.assertIn(Block(RangeSet("5-7, 22-24, 37-39")), blocks) # g h i
        self.assertIn(Block(RangeSet("10-14, 25-29, 40-44")), blocks) # ! q r s t
        self.assertIn(Block(RangeSet("4, 21")), blocks) # F


