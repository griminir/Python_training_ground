'''learning about exceptions'''
# numbers = [1,2]
# print(numbers[3])

try:
    with open('exceptions.py') as file:
        print('file opened.')
    age = int(input('age: '))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print('you did not enter a valid age')
else:
    print(f'no expections where thrown and age is {age}')
from timeit import timeit

code1 = '''
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('age can not be zero or less')
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
'''

code2 = '''
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

    
xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
'''

print('first code:', timeit(code1, number=10000))
print('second code:', timeit(code2, number=10000))
