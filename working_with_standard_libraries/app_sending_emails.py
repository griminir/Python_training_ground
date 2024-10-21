from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

# how to set up app password
# https://www.youtube.com/watch?v=Y_u5KIeXiVI&ab_channel=DAIMTODeveloperTips

template = Template(Path('template.html').read_text())
body = template.substitute({'name': 'erlend'})

message = MIMEMultipart()
message['from'] = 'python script by viktor'
message['to'] = 'reciver email'
message['subject'] = 'python msg'
message.attach(MIMEText('this should be the body of the msg', 'plain'))
# message.attach(MIMEText(body, 'html')) # this is the way to do it with variables and different things
# for adding image
# message.attach(MIMEImage(Path('meme.png').read_bytes()))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # hello msg needed for starting it
    smtp.ehlo()
    # tls = transport layer security encrypts the info
    smtp.starttls()
    # login
    smtp.login('gmail with 2factor', 'app password')
    smtp.send_message(message)
    print('sent....')
