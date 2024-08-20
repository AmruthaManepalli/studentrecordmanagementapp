import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,body,subject):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('manepalliamrutha1402@gmail.com','nghb qqqd jifb ihnl')
    msg=EmailMessage()
    msg['FROM']='manepalliamrutha1402@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()    