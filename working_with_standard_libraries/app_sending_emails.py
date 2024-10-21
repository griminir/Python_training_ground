from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# how to set up app password
# https://www.youtube.com/watch?v=Y_u5KIeXiVI&ab_channel=DAIMTODeveloperTips

message = MIMEMultipart()
message['from'] = 'python script by viktor'
message['to'] = 'email you are sending to'
message['subject'] = 'python msg'
message.attach(MIMEText('this should be the body of the msg'))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # hello msg needed for starting it
    smtp.ehlo()
    # tls = transport layer security encrypts the info
    smtp.starttls()
    # login
    smtp.login('email that has 2factor and kan make app passwords',
               'app password')
    smtp.send_message(message)
    print('sent....')
