import random
import string

print(random.random())
print(random.randint(1, 10))  # 1 - 10
print(random.choice([1, 4, 5, 9]))  # pick one from the array
# pick amount equal to k from the array
print(random.choices([1, 4, 5, 9], k=2))
print(''.join(random.choices(string.ascii_letters + string.digits, k=12))) # start to a password generator?

numbers = [1,2,3,4]
random.shuffle(numbers)
print(numbers)