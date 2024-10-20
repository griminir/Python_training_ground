"""other filled started to get to filled"""
from collections import deque
from array import array
# queues (FIFO = First In First Out)
# the import of deque helps with preformance (example large lists)
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()  # special deque method
print(queue)
if not queue:
    print('empty')


# tuples can not be modified so use them when you dont want data to get change
point = (1, 2, 3)
x = 5
y = 10
x, y = y, x
print(f'y: {y}, x:{x} as you can see they are not the same value as originally stated, they have been swapped')

# arrays better for large list of numbers > 10000 ish (use only if you are having preformance problems)
# need to be imported
# need a type code for the array google it lowercase i is for int
numbers = array('i', [1, 2, 3])
# works like a list but is strongly typed, the list can only contain items of the correct data type

# sets
numbers_2 = [1,2,3,4,3,5,5,2,2]
first = set(numbers_2)
second = {1, 6, 3}
# print(first)
print(first | second) # both sets together but only uniques
print(first & second) # only items in that is in both sets
print(first - second) # only items that are in first but not second
print(first ^ second) # all the items that are unique for either first or second
# cant use index so we use 
if 1 in first: 
    print('yes')


# dictioraries are key:value pairs
point2 = dict(x=1, Y=2)
print(f'{point2['x']} from dictonary')
point2['z'] = 20
point2['x'] = 10
if 'a' in point2:
    print(point2['a'])
print(point2.get('a', 'does not exist'))
del point2['x']
print(point2)
for key in point2:
    print(key, point2[key])

# unpacking operator dictonaries needs ** for unpacking
print(numbers_2)
print(*numbers_2)
values = [*range(5), *'hello']
print(values)


# exercise write programm that finds the most repeated letter in a text
from pprint import pprint # can be used to make things look prettier in the output
sentence = "this is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(), 
    key=lambda kv:kv[1], 
    reverse=True)
print(char_frequency_sorted[0])

