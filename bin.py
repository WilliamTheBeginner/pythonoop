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
split56 = Outcome('Split 5-6', 17)
split58 = Outcome('Split 5-8', 17)
split69 = Outcome('Split 6-9', 17)
split47 = Outcome('Split 4-7', 17)
split78 = Outcome('Split 7-8', 17)
split710 = Outcome('Split 7-10', 17)
split89 = Outcome('Split 8-9', 17)
split811 = Outcome('Split 8-11', 17)
split912 = Outcome('Split 9-12', 17)
split1011 = Outcome('Split 10-11', 17)
split1013 = Outcome('Split 10-13', 17)
split1112 = Outcome('Split 11-12', 17)
split1114 = Outcome('Split 11-14', 17)
split1215 = Outcome('Split 12-15', 17)

street123 = Outcome('Street 1-2-3', 11)
street456 = Outcome('Street 4-5-6', 11)
street789 = Outcome('Street 7-8-9', 11)
street101112 = Outcome('Street 10-11-12', 11)

corner1245 = Outcome('Corner 1-2-4-5', 8)
corner2356 = Outcome('Corner 2-3-5-6', 8)
corner4578 = Outcome('Corner 4-5-7-8', 8)
corner5689 = Outcome('Corner 5-6-8-9', 8)
corner781011 = Outcome('Corner 7-8-10-11', 8)
corner891112 = Outcome('Corner 8-9-11-12', 8)
corner10111314 = Outcome('Corner 10-11-13-14', 8)
corner11121415 = Outcome('Corner 11-12-14-15', 8)

five = Outcome('00-0-1-2-3', 6)

line123456 = Outcome('Line 1-2-3-4-5-6', 5)
line456789 = Outcome('Line 4-5-6-7-8-9', 5)
line789101112 = Outcome('Line 7-8-9-10-11', 5)
line101112131415 = Outcome('Line 10-11-12-13-14-15', 5)

zero = Bin([Outcome('0', 35), five])
zerozero = Bin([Outcome('00', 35), five])
one = Bin([Outcome('1', 35), red, low, odd, dozen_1, column_1, split12, split14, street123, corner1245, five, line123456])
two = Bin([Outcome('2', 35), black, low, even, dozen_1, column_2, split12, split23, split25, street123, corner1245, corner2356, five, line123456])
three = Bin([Outcome('3', 35), red, low, odd, dozen_1, column_3, split23, split36, street123, corner2356, five, line123456])
four = Bin([Outcome('4', 35), black, low, even, dozen_1, column_1, split14, split45, split47, street456, corner1245, corner4578, line123456, line456789])
five = Bin([Outcome('5', 35), red, low, odd, dozen_1, column_2, split45, split25, split56, split58, street456, corner1245, corner2356, corner4578, corner5689, line123456, line456789])
six = Bin([Outcome('6', 35), black, low, even, dozen_1, column_3, split36, split56, split69, street456, corner2356, corner5689, line456789])
seven = Bin([Outcome('7', 35), red, low, odd, dozen_1, column_1, split47, split78, split710, street789, corner781011, corner4578, line456789, line789101112])
eight = Bin([Outcome('8', 35), black, low, even, dozen_1, column_2, split78, split58, split89, split811, street789, corner5689, corner4578, corner891112, corner781011, line456789, line789101112])
nine = Bin([Outcome('9', 35), red, low, odd, dozen_1, column_3, split89, split69, split912, street789, corner5689, corner891112, line456789, line789101112])
ten = Bin([Outcome('10', 35), black, low, even, dozen_1, column_1, split710, split1011, split1013, street101112, corner781011, corner10111314, line789101112, line101112131415])
eleven = Bin([Outcome('11', 35), black, low, odd, dozen_1, column_2, split811, split1011, split1112, split1114, street101112, corner781011, corner10111314, corner891112, corner11121415, line789101112, line101112131415])
twelve = Bin([Outcome('12', 35), red, low, even, dozen_1, column_3, split912, split1112, split1215, street101112, corner891112, corner11121415, line789101112, line101112131415])
thirteen = Bin([Outcome('13' 35), black, low, odd, dozen_2, column_1, split1013, split1314, split1316, street131415, st])
