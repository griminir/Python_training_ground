"""loop training"""
# Probably better to use number or index
success = False
for salami in range(3):
    print('We have tried reaching to about of your car\'s extender warrenty, attempt:', salami + 1)
    if success:
        print('thank you for your extension')
        break
else:
    print('we added it to your car anyway\'s')

for x in range(5):
    for y in range(3):
        print(f'({x}, {y})')

number = 100
while number > 0:
    print(number)
    number //= 2

# command = ''
# while command.lower() != 'quit':
#     command = input('>')
#     print('ECHO', command)

# while True:
#     user_input = input('>')
#     print('ECHO', user_input)
#     if user_input.lower() == 'quit':
#         break

count = 0
for number in range(1, 10):
    
    if number % 2 == 0:
        print(number)
        count += 1
print(f'we have {count} even numbers')
