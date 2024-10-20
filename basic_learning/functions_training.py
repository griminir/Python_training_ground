"""function training"""


def greet(first_name, last_name):
    print(f'Hello {first_name}')
    print(f'time to learn Mr.{last_name}')


greet('viktor', 'degray')


def get_name(name='stranger'):
    return name


print(get_name(name='viktor'))
print(get_name())

# xargs


def multiply(*numbers):
    output = 1
    for number in numbers:
        output *= number
    return output


print('start')
print(multiply(1, 45, 5))

# xxargs


def save_user(**user):
    print(user)


save_user(id=1, name='timmy', age=33)


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'fizzbuzz'
    if input % 3 == 0:
        return 'fizz'
    if input % 5 == 0:
        return 'buzz'
    return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
