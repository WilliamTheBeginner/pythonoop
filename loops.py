nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

stop = '--------------------'

print(stop)

for num in nums:
    if num == 3:
        break
    print(num)

# the continue statement will skip to the next iteration of the loop

print(stop)

for num in nums:
    if num == 3:
        continue
    print(num)

# example of a loop in a loop

for num in nums:
    for letter in 'abc':
        print(num, letter)

# sometimes we just want to run through a loop a CERTAIN number of times



x = 10

while True:
    #if x == 5:
    #    break
    print(x)
    x += 1

#ctrl -c can interrupt the loops
