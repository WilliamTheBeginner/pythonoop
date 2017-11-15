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
split23 = Outcome('Split 2-3', 17)
split25 = Outcome('Split 2-5', 17)
split36 = Outcome('Split 3-6', 17)
split45 = Outcome('Split 4-5', 17)

street123 = Outcome('Street 1-2-3', 11)
street456 = Outcome('Street 4-5-6', 11)

corner1245 = Outcome('Corner 1-2-4-5', 8)
corner2356 = Outcome('Corner 2-3-5-6', 8)
corner4578 = Outcome('Corner 4-5-7-8', 8)

five = Outcome('00-0-1-2-3', 6)

line123456 = Outcome('Line 1-2-3-4-5-6', 5)
line456789 = Outcome('Line 4-5-6-7-8-9', 5)

zero = Bin([Outcome('0', 35), five])
zerozero = Bin([Outcome('00', 35), five])
one = Bin([Outcome('1', 35), red, low, odd, dozen_1, column_1, split12, split14, street123, corner1245, five, line123456])
two = Bin([Outcome('2', 35), black, low, even, dozen_1, column_1, split12, split23, split25, street123, corner1245, corner2356, five, line123456])
three = Bin([Outcome('3', 35), red, low, odd, dozen_1, column_1, split23, split36, street123, corner2356, five, line123456])
four = Bin([Outcome('4', 35), black, low, even, dozen_1, column_1, split14, split45, street456, corner1245, corner4578, line123456, ])
