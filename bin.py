from outcome import Outcome

class Bin(frozenset):
    pass

# a spin of 1 reflects the 1 bin and the outcomes in the bin
# all the outcomes of 1 are collected in a single bin
