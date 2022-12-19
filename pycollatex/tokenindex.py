from ClusterShell.RangeSet import RangeSet
from pycollatex.block import Block
from pycollatex.core_classes import Token
from pycollatex.linsuffarr import SuffixArray
from pycollatex.linsuffarr import UNIT_BYTE


class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]


# TokenIndex
class TokenIndex(object):
    def __init__(self, collation):
        self.witnesses = collation.witnesses
        self.vocabulary = collation.vocabulary
        # print("\nwitnesses=",witnesses)
        self.counter = 0
        self.witness_ranges = {}
        self.token_array = []
        self.witness_to_block_instances = {}
        self.suffix_array = []
        self.lcp_array = []
        self.blocks = []

    def prepare(self):
        self._prepare_token_array()
        # print("> self.token_array=", self.token_array)
        # call third party library here
        self.suffix_array = self.get_suffix_array()
        self.lcp_array = self.get_lcp_array()
        self.blocks = self.split_lcp_array_into_intervals()
        self.construct_witness_to_block_instances_map()

    @classmethod
    def create_token_index(cls, collation):
        token_index = TokenIndex(collation.witnesses)
        token_index.prepare()
        return token_index

    def _prepare_token_array(self):
        # TODO: the lazy init should move to somewhere else
        # clear the suffix array and LCP array cache
        self.cached_suffix_array = None
        token_array_position = 0
        for idx, witness in enumerate(self.witnesses):
            # print("witness.tokens",witness.tokens())
            witness_range = RangeSet()
            witness_range.add_range(self.counter, self.counter + len(witness.tokens()))
            # the extra one is for the marker token
            self.counter += len(witness.tokens()) + 1
            self.witness_ranges[witness.sigil] = witness_range
            # remember get tokens twice
            sigil = witness.sigil
            for token in witness.tokens():
                token._token_array_position = token_array_position
                token_array_position += 1
            self.token_array.extend(witness.tokens())
            # # add marker token
            self.token_array.append(Token(self.vocabulary.encode('$' + str(idx)), witness.sigil))
            token_array_position += 1
        self.token_array.pop()  # remove last marker

    def split_lcp_array_into_intervals(self):
        closed_intervals = []
        previous_lcp_value = 0
        open_intervals = Stack()
        for idx in range(0, len(self.lcp_array)):
            lcp_value = self.lcp_array[idx]
            if lcp_value > previous_lcp_value:
                open_intervals.push(Block(self, start=idx - 1, length=lcp_value))
                previous_lcp_value = lcp_value
            elif lcp_value < previous_lcp_value:
                #         close open intervals that are larger than current LCP value
                while open_intervals and open_intervals.peek().length > lcp_value:
                    a = open_intervals.pop()
                    closed_intervals.append(Block(self, start=a.start, end=idx - 1, length=a.length))

                # then: open a new interval starting with filtered intervals
                if lcp_value > 0:
                    start = closed_intervals[len(closed_intervals) - 1].start
                    open_intervals.push(Block(self, start=start, length=lcp_value))

                previous_lcp_value = lcp_value

        # add all the open intervals to the result
        # print("> open_intervals=", open_intervals)
        # print("> closed_intervals=", closed_intervals)
        for interval in open_intervals:
            if interval.length > 0:
                closed_intervals.append(
                    Block(self, start=interval.start, end=len(self.lcp_array) - 1, length=interval.length))
        # print("> closed_intervals=", closed_intervals)
        return closed_intervals

    def get_range_for_witness(self, witness_sigil):
        if witness_sigil not in self.witness_ranges:
            raise Exception("Witness " + witness_sigil + " is not added to the collation!")
        return self.witness_ranges[witness_sigil]

    def get_sa(self):
        # NOTE: implemented in a lazy manner, since calculation of the Suffix Array and LCP Array takes time
        # print("token_array=",self.token_array)
        # for token in self.token_array:
        #     print(token,":",type(token))
        if not self.cached_suffix_array:
            # string_array = ''.join([token.token_string for token in self.token_array])
            string_array = [token.token_string for token in self.token_array]
            # Unit byte is done to skip tokenization in third party library
            ##print("> string_array =", string_array)
            self.cached_suffix_array = SuffixArray(string_array, unit=UNIT_BYTE)
            ##print("> suffix_array:\n", self.cached_suffix_array)
        return self.cached_suffix_array

    def get_suffix_array(self):
        sa = self.get_sa()
        return sa.SA

    def get_lcp_array(self):
        sa = self.get_sa()
        return sa._LCP_values

    def start_token_position_for_witness(self, witness):
        return self.get_range_for_witness(witness.sigil)[0]

    def block_instances_for_witness(self, witness):
        return self.witness_to_block_instances.setdefault(witness.sigil, [])

    def construct_witness_to_block_instances_map(self):
        self.witness_to_block_instances = {}
        ##print("> self.blocks", self.blocks)
        for interval in self.blocks:
            for instance in interval.get_all_instances():
                ##print(">instance = ", instance)
                w = instance.get_witness_sigil()
                instances = self.witness_to_block_instances.setdefault(w, [])
                instances.append(instance)

    # factory method for testing purposes only!
    @classmethod
    def for_test(cls, sa_array, lcp_array):
        token_index = TokenIndex(None)
        token_index.suffix_array = sa_array
        token_index.lcp_array = lcp_array
        return token_index  # parts of the LCP array become potential blocks.