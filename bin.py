from outcome import Outcome
# a spin of 1 reflects the 1 bin and the outcomes in the bin
# all the outcomes of 1 are collected in a single bin
class Bin(frozenset):
    pass

red = Outcome('Red', 1)
black = Outcome('Black', 1)

low = Outcome('low', 1)
high = Outcome('high', 1)

even = Outcome('Even', 1)
odd = Outcome('Odd', 1)

dozen_1 = Outcome('1 Dozen', 2)
dozen_2 = Outcome('2 Dozen', 2)
dozen_3 = Outcome('3 Dozen', 2)

column_1 = Outcome('1 Column', 2)
column_2 = Outcome('2 Column', 2)
column_3 = Outcome('3 Column', 2)

split12 = Outcome('Split 1-2', 17)
split14 = Outcome('Split 1-4', 17)

street123 = Outcome('Straight 1-2-3', 11)

corner1245 = Outcome('Corner 1-2-4-5', 8)

five = Outcome('00-0-1-2-3', 6)

line123456 = Outcome('Line 1-2-3-4-5-6', 5)

one = Bin([Outcome('1', 35), red, low, odd, dozen_1, column_1, split12, split14, street123, corner1245, five, line123456])
