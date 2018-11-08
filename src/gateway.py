# import email client class

class CarrierGateway(SMS):
	
	def __init__(self):
		pass

	def connect(self):
		self._client = Email()

	def send(self, dest_num, msg):
		dest = "{}@{}".format(dest_num, self._gateway)
		self._client.send(dest, msg)
