import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configura los detalles del servidor
smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_user = 'juliandge@outlook.com'  # Asegúrate de que sea tu correo de Outlook
smtp_password = 'qdeu ikph hvdt fwuz'  # Usa la contraseña de aplicación aquí

# Configura los detalles del mensaje
msg = MIMEMultipart()
msg['From'] = 'juliandge@outlook.com'  # Asegúrate de que coincida con smtp_user
msg['To'] = 'nicolasrodriguezt@ucundinamarca.edu.co'
msg['Subject'] = 'ALERTA TEMPRANA ACCESO A AULAS CMA DIGITAL'

# Añade el cuerpo del mensaje
body = 'Este es el cuerpo del correo.'
msg.attach(MIMEText(body, 'plain'))

# Conecta al servidor SMTP y envía el correo
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Usa TLS para la conexión segura
    server.login(smtp_user, smtp_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("Correo enviado con éxito")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
finally:
    server.quit()
