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
split1314 = Outcome('Split 13-14', 17)
split1316 = Outcome('Split 13-16', 17)
split1415 = Outcome('Split 14-15', 17)
split1417 = Outcome('Split 14-17', 17)
split1518 = Outcome('Split 15-18', 17)
split1617 = Outcome('Split 16-17', 17)
split1619 = Outcome('Split 16-19', 17)
split1718 = Outcome('Split 17-18', 17)
split1720 = Outcome('Split 17-20', 17)
split1821 = Outcome('Split 18-21', 17)
split1920 = Outcome('Split 19-20', 17)
split1922 = Outcome('Split 19-22', 17)
split2021 = Outcome('Split 20-21', 17)
split2023 = Outcome('Split 20-23', 17)
split2124 = Outcome('Split 21-24', 17)
split2223 = Outcome('Split 22-23', 17)
split2225 = Outcome('Split 22-25', 17)
split2324 = Outcome('Split 23-24', 17)
split2326 = Outcome('Split 23-26', 17)
split2427 = Outcome('Split 24-27', 17)
split2526 = Outcome('Split 25-26', 17)
split2528 = Outcome('Split 25-28', 17)

street123 = Outcome('Street 1-2-3', 11)
street456 = Outcome('Street 4-5-6', 11)
street789 = Outcome('Street 7-8-9', 11)
street101112 = Outcome('Street 10-11-12', 11)
street131415 = Outcome('Street 13-14-15', 11)
street161718 = Outcome('Street 16-17-18', 11)
street192021 = Outcome('Street 19-20-21', 11)
street222324 = Outcome('Street 22-23-24', 11)


corner1245 = Outcome('Corner 1-2-4-5', 8)
corner2356 = Outcome('Corner 2-3-5-6', 8)
corner4578 = Outcome('Corner 4-5-7-8', 8)
corner5689 = Outcome('Corner 5-6-8-9', 8)
corner781011 = Outcome('Corner 7-8-10-11', 8)
corner891112 = Outcome('Corner 8-9-11-12', 8)
corner10111314 = Outcome('Corner 10-11-13-14', 8)
corner11121415 = Outcome('Corner 11-12-14-15', 8)
corner13141617 = Outcome('Corner 13-14-16-17', 8)
corner14151718 = Outcome('Corner 14-15-17-18', 8)
corner16171920 = Outcome('Corner 16-17-19-20', 8)
corner17182021 = Outcome('Corner 17-18-20-21', 8)
corner19202223 = Outcome('Corner 19-20-22-23', 8)
corner20212324 = Outcome('Corner 20-21-23-24', 8)
corner22232526 = Outcome('Corner 22-23-25-26', 8)
corner23242627 = Outcome('Corner 23-24-26-27', 8)

five = Outcome('00-0-1-2-3', 6)

line123456 = Outcome('Line 1-2-3-4-5-6', 5)
line456789 = Outcome('Line 4-5-6-7-8-9', 5)
line789101112 = Outcome('Line 7-8-9-10-11', 5)
line101112131415 = Outcome('Line 10-11-12-13-14-15', 5)
line131415161718 = Outcome('Line 13-14-15-16-17-18', 5)
line161718192021 = Outcome('Line 16-17-18-19-20-21', 5)
line192021222324 = Outcome('Line 19-20-21-22-23-24', 5)
line222324252627 = Outcome('Line 22-23-24-25-26-27', 5)

zero = Bin([Outcome('0', 35), five])
zerozero = Bin([Outcome('00', 35), five])
one = Bin([Outcome('1', 35), red, low, odd, dozen_1, column_1,
           split12, split14, street123, corner1245, five, line123456])
two = Bin([Outcome('2', 35), black, low, even, dozen_1, column_2, split12,
           split23, split25, street123, corner1245, corner2356, five, line123456])
three = Bin([Outcome('3', 35), red, low, odd, dozen_1, column_3,
             split23, split36, street123, corner2356, five, line123456])
four = Bin([Outcome('4', 35), black, low, even, dozen_1, column_1, split14, split45,
            split47, street456, corner1245, corner4578, line123456, line456789])
five = Bin([Outcome('5', 35), red, low, odd, dozen_1, column_2, split45, split25, split56,
            split58, street456, corner1245, corner2356, corner4578, corner5689, line123456, line456789])
six = Bin([Outcome('6', 35), black, low, even, dozen_1, column_3, split36,
           split56, split69, street456, corner2356, corner5689, line456789])
seven = Bin([Outcome('7', 35), red, low, odd, dozen_1, column_1, split47, split78,
             split710, street789, corner781011, corner4578, line456789, line789101112])
eight = Bin([Outcome('8', 35), black, low, even, dozen_1, column_2, split78, split58, split89,
             split811, street789, corner5689, corner4578, corner891112, corner781011, line456789, line789101112])
nine = Bin([Outcome('9', 35), red, low, odd, dozen_1, column_3, split89, split69,
            split912, street789, corner5689, corner891112, line456789, line789101112])
ten = Bin([Outcome('10', 35), black, low, even, dozen_1, column_1, split710, split1011,
           split1013, street101112, corner781011, corner10111314, line789101112, line101112131415])
eleven = Bin([Outcome('11', 35), black, low, odd, dozen_1, column_2, split811, split1011, split1112, split1114,
              street101112, corner781011, corner10111314, corner891112, corner11121415, line789101112, line101112131415])
twelve = Bin([Outcome('12', 35), red, low, even, dozen_1, column_3, split912, split1112,
              split1215, street101112, corner891112, corner11121415, line789101112, line101112131415])
thirteen = Bin([Outcome('13', 35), black, low, odd, dozen_2, column_1, split1013, split1314,
                split1316, street131415, corner10111314, corner13141617, line101112131415, line131415161718])
fourteen = Bin([Outcome('14', 35), red, low, even, dozen_2, column_2, split1314, split1114, split1415, split1417,
                street131415, corner10111314, corner11121415, corner14151718, corner13141617, line101112131415, line131415161718])
fifteen = Bin([Outcome('15', 35), black, low, odd, dozen_2, column_3, split1215, split1415,
               split1518, street131415, corner11121415, corner14151718, line101112131415, line131415161718])
sixteen = Bin([Outcome('16', 35), red, low, even, dozen_2, column_1, split1316, split1617,
               split1619, street161718, corner13141617, corner16171920, line131415161718, line161718192021])
seventeen = Bin([Outcome('17', 35), black, low, odd, dozen_2, column_2, split1417, split1617, split1718, split1720,
                 street161718, corner14151718, corner17182021, corner13141617, corner16171920, line131415161718, line161718192021])
eighteen = Bin([Outcome('18', 35), red, low, even, dozen_2, column_3, split1718, split1518,
                split1821, street161718, corner14151718, corner17182021, line131415161718, line161718192021])
nineteen = Bin([Outcome('19', 35), black, high, odd, dozen_2, column_1, split1619, split1920,
                split1922, street192021, corner19202223, corner16171920, line161718192021, line192021222324])
twenty = Bin([Outcome('20', 35), black, high, even, dozen_2, column_2, split1920, split1720, split2021, split2023,
              corner16171920, corner17182021, corner20212324, corner19202223, street192021, line161718192021, line192021222324])
twenty_one = Bin([Outcome('21', 35), red, high, odd, dozen_2, column_3, split1821, split2021,
                  split2124, street192021, corner17182021, corner20212324, line161718192021, line192021222324])
twenty_two = Bin([Outcome('22', 35), black, high, even, dozen_2, column_1, split1922, split2223,
                  split2225, street222324, corner19202223, corner22232526, line192021222324, line222324252627])
twenty_three = Bin([Outcome('23', 35), red, high, odd, dozen_2, column_2, split2023, split2223, split2324, split2326,
                    street222324, corner19202223, corner22232526, corner23242627, corner20212324, line192021222324, line222324252627])
twenty_four = Bin([Outcome('24', 35), black, high, even, dozen_2, column_3, split2124, split2324,
                   split2427, street222324, corner20212324, corner23242627, line192021222324, line222324252627])
twenty_five = Bin([Outcome('25', 35), red, high, odd, dozen_3, column_1, split2526, split2225,
                   split2528, street252627, corner22232526, corner25262829, line222324252627, line252627282930])
twenty_six = Bin([Outcome('26', 35), black, high, even, dozen_3, column_2, split2326, split2526, split2627, split2629,
                  street252627, corner22232526, corner23242627, corner26272930, corner25262829, line2223242526, line252627282930])
twenty_seven = Bin([Outcome('27', 35), red, high, odd, dozen_3, column_3, split2427, split2627,
                    split2730, street252627, corner23242627, corner26272930, line222324252627, line252627282930])
twenty_eight = Bin([Outcome('28', 35), red, high, even, dozen_3, column_1, split2528, split2829,
                    split2931, street282930, corner25262829, corner28293132, line252627282930, line282930313233])
twenty_nine = Bin([Outcome('29', 35), black, high, odd, dozen_3, column_2, split2829, split2629, split2930, split2932,
                   street282930, corner25262829, corner26272930, corner29303233, corner28293132, line252627282930, line282930313233])
thirty = Bin([Outcome('30', 35), red, high, even, dozen_3, column_3, split2730, split2930,
              split3033, street282930, corner26272930, corner29303233, line252627282930, line282930313233])
thirty_one = Bin([Outcome('31', 35), black, odd, dozen_3, column_1, split2831, split3132,
                  split3134, street313233, corner28293132, corner31323435, line282930313233, line313233343536])
thirty_two = Bin([Outcome('32', 35), red, even, dozen_3, column_2, split2932, split3233, split3132, split3235,
                  street313233, corner29303233, corner28293132, corner32333536, corner31323435, line282930313233, line313233343536])
thirty_three = Bin([Outcome('33', 35), black, odd, dozen_3, column_3, split3033, split3233,
                    split3336, street313233, corner29303233, corner32333536, line282930313233, line313233343536])
thirty_four = Bin([Outcome('34', 35), red, even, dozen_3, column_1, split3134,
                   split3435, street343536, corner31323435, line313233343536])
thirty_five = Bin([Outcome('35', 35), black, odd, dozen_3, column_2, split3435, split3235,
                   split3536, street343536, corner31323435, corner32333536, line313233343536])
thirty_six = Bin([Outcome('36', 35), red, even, dozen_3, column_3, split3336,
                  split3536, street343536, corner32333536, line313233343536])
