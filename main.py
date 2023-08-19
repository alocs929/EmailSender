import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email ="from@gmail.com"
senha = "" 
destino = "to@gmail.com"

try:
    conexao = smtplib.SMTP("smtp.gmail.com", 587)
    conexao.starttls()
    conexao.login(user=email, password=senha)

    mensagem = MIMEMultipart()
    mensagem['Subject'] = "Importante!"
    mensagem['From'] = email
    mensagem['To'] = destino
    corpo_mensagem = "Olá, você não sabe mandar email com python 😄"
    mensagem.attach(MIMEText(corpo_mensagem, 'plain', 'utf-8'))

    conexao.sendmail(from_addr=email, to_addrs=destino, msg=mensagem.as_string())
    print(f'Email enviado com sucesso! Destino: {destino}' )

except Exception as e:
    print("Ocorreu um erro:", e)
finally:
    conexao.quit()
