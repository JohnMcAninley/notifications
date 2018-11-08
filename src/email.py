import email
import smptlib

class ExtEmail(Channel):
	
	def __init__(self):
		pass

	def connect(self):
		pass

	def send(self, dest, msg):
	
		mail = email.MIMEText(msg)
		mail['From'] = self._email_address		
		mail['To'] = dest

		# connect to mail server
		server = smtplib.SMTP_SSL(mail_server)
		# TODO remove hostname from initialization
		# self._client.connect(self._server)
		server.ehlo()
		server.login(
			self._creds.username, 
			self._creds.password)

		# send
		text = mail.as_string()
		server.sendmail(email_address, dest, text)

		# disconnect
		server.quit()
