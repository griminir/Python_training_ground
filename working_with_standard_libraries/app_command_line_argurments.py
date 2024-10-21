import sys

if len(sys.argv) == 1:
    print('USAGE: python app_command_line_argurments.py <password>')
else:
    password = sys.argv[1]
    print('password', password)
