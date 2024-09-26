import smtplib 
from email.mime.multipart import MIMEMultipart #Classe que permite textos e anexos no email 
from email.mime.text import MIMEText #Classe que cria corpo do email em formato de texto

import pandas as pd

remetente = 'vinicusm466@gmail.com'
destinatario = 'vinicusm466@gmail.com'
assunto = 'Teste de envio de e-mail'
corpo = 'Olá, este é um e-mail enviado através de Python!'
df = pd.read_excel('/c/Users/Users/Documents/MeusProjetos/automatizacao-email/bdTeste.xlsx')

msg = MIMEMultipart()
msg['From'] = remetente
msg['To'] = destinatario
msg['Subject'] = assunto
msg.attach(MIMEText(corpo, 'plain'))

# Servidor SMTP
smtp_server = 'smtp.gmail.com'
porta = 587
senha = 'wxqx mesf afln qpaf'

try:
    servidor = smtplib.SMTP(smtp_server, porta)
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.send_message(msg)
    print('E-mail enviado com sucerro!')
except Exception as e:
    print(f'Falha ao enviar o e-mail: {e}')
finally:
    servidor.quit()