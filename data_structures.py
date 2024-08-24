"""learning different data structures"""

letters = ['a', 'b', 'c']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 10
combined = zeros + letters


numbers = list(range(0, 20))

# print(zeros)
# print(combined)
# print(numbers)
# print(len(numbers))
# print(numbers[::2])
# print(numbers[::-1])

# unpacking lists
first, *rest, last = numbers
# print(first, last)
# print(rest)

# looping over lists


def loop_list(list):
    # unpacking of the tuple that enumerate makes
    for index, item in enumerate(list):
        print(index, item)

# loop_list(numbers)

# adding and removing


def adding_to_list(list):
    # add at the end
    list.append('appended')
    list.insert(0, 'inserted')
    list.insert(3, 'inserted at 4th place')
    print(list)


# adding_to_list(numbers)

def removing_from_list(list):
    # removes at end or if arg added removes at index
    list.pop()
    # removes the first instance of arg
    list.remove(5)
    # deleting an index or a range
    del list[0:3]
    print(list)
    # removes every item in a list
    list.clear()
    print(list)

# removing_from_list(numbers)

# finding stuff in a list


def list_find(list):
    # done to not get the error
    if 5 in list:
        print(list.index(5))

# list_find(numbers)

#sorting lists
random_numbers = [3, 6, 1, 8, 4, 10]
new_sorted_list = sorted(random_numbers)
random_numbers.sort(reverse=True)
# print(random_numbers)
# print(new_sorted_list)  

items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12)
]
#basic way of doing it
# def sort_items(item):
#     return item[1]

#better way of doing it
items.sort(key=lambda item: item[1])
# print(items)

#map
prices = list(map(lambda item: item[1], items))
#list comprehension way (better practice in python)
prices = [item[1] for item in items]
print(prices)

#filter
filtered = list(filter(lambda item: item[1] >= 10, items))
#list comprehension way (better practice in python)
filtered = [item for item in items if item[1] >= 10]
print(filtered)
