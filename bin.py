from outcome import Outcome
# a spin of 1 reflects the 1 bin and the outcomes in the bin
# all the outcomes of 1 are collected in a single bin
class Bin(frozenset):
    pass

five = Bin([Outcome('00-0-1-2-3', 6)])
zero = Bin([Outcome('0', 35), five])
zerozero = Bin([Outcome('00', 35), five])
