import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Importando os dados
from analysing_cpu import CPU
from analysing_disk import Disk
from analysing_memory import Memory
from analysing_network import Network


def Email():
    # Mensagem que aparecera no email
    mail_content = CPU() + Disk() + Memory() + Network()

    # Senha e email utilizado para enviar
    sender_address = 'email@email.com'
    sender_pass = '12345'

    # Email de quem vai receber
    receiver_address = 'email@email.com'

    # Utilizando o MIMEMultipar
    message = MIMEMultipart()

    # Enviando o email
    message['From'] = sender_address
    message['To'] = receiver_address

    # Subtitulo do email
    message['Subject'] = 'Desafio dados do pc'

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    # Criando uma smtp com uma porta para enviar o email é possível entender
    # melhor
    #  no link https://support.google.com/mail/answer/7126229?hl=pt-BR&
    # authuser=3
    # Passando o smtp e a porta dele
    session = smtplib.SMTP('smtp.gmail.com', 587)

    # Habilitando a segurança
    session.starttls()

    # Realizando login
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    print('Email enviado com Sucesso')

schedule.every().hour.do(Email)

while True:
    schedule.run_pending()
    time.sleep(1)

# Email()