temprature = 35
if temprature > 25:
    print('it\'s warm')
    print('drink water')
elif temprature > 20:
    print('perfect temp')
else:
    print('can\'t be sommer')
print('done')

age = 22
# ternary operator
message = 'can drink' if age >= 18 else 'can\'t drink'
print(message)

# chaining comparison operators
if 18 <= age < 65:
    print('Probably working')

# logical operators: and, or, not
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print('Eligible')
else:
    print('Not eligible')
