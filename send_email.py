import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send(nome, idade, manha):
    # Configurações do remetente
    remetente_email = "memeshaha132@gmail.com"
    remetente_senha = "kcqw zzvu fqwa gllh"

    # Configurações do destinatário
    destinatario_email = "thiagolcsalves@gmail.com"

    # Configurações do servidor SMTP do Gmail
    smtp_servidor = "smtp.gmail.com"
    smtp_porta = 587

    # Criação da mensagem
    assunto = f"Informações do paciente: {nome}"
    corpo = f"Nome completo: {nome} \nIdade: {idade} \n\nCafe da manhã: {manha}"

    mensagem = MIMEMultipart()
    mensagem['From'] = remetente_email
    mensagem['To'] = destinatario_email
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(corpo, 'plain'))

    # Conexão com o servidor SMTP
    try:
        servidor_smtp = smtplib.SMTP(smtp_servidor, smtp_porta)
        servidor_smtp.starttls()  # Inicia a camada de segurança TLS
        servidor_smtp.login(remetente_email, remetente_senha)
        
        # Envio do e-mail
        servidor_smtp.sendmail(remetente_email, destinatario_email, mensagem.as_string())
        
        print("E-mail enviado com sucesso!")

    except Exception as e:
        print("Erro ao enviar o e-mail:", str(e))

    finally:
        # Fecha a conexão com o servidor SMTP
        if servidor_smtp:
            servidor_smtp.quit()
