import pandas as pd
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def enviaemail(member): 
   for index, members in member.iterrows():
    #print(members) lista de objetos
  
    host = 'smtp.gmail.com'
    port = '587'
    login = 'informa o email de acesso'
    password = 'informe a senha de acesso' #peça para secretario geral da aaaccnavegadores.
    
    server = smtplib.SMTP(host,port)
    
    server.ehlo()
    server.starttls()
    server.login(login,password)
  
  
    corpo = f"Olá {members ['Nome']}, você recebeu um email da Navegadores em Teste!"
    
    email_msg = MIMEMultipart()
    
    email_msg['From'] =  'aaaccnavegadores@gmail.com' #Quem está mandando o email
    
    email_msg['To'] = members['Email'] #Substitui um email fixo pelo vindo na função.
    
    email_msg['Subject'] = 'Assunto do email' # Tipo do assunto
    
    email_msg.attach(MIMEText(corpo,'plain'))
    
    
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    print("Emails enviado com sucesso!")
    server.quit() 
  
  

#Iniciando um por um de membro
member = pd.read_excel('./src/entrada.xlsx') 
enviaemail(member)
    

    