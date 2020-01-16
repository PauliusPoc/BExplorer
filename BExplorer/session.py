import paramiko
import sys
import ast

class Client:
	def __init__(self):
		self.username = 'user019' 
		self.password = 'pCS0B4kn'
		self.hostname = '158.129.140.201'
		self.port = 3637
		self.nbytes = 4096
		self.client = None
		self.session = None

	def create_session(self):
		if self.client is None:
			self.client = paramiko.Transport((self.hostname, self.port))
			self.client.connect(username=self.username, password=self.password)
			self.session = self.client.open_channel(kind='session')

	def execute_command(self, command):
		if self.client is not None:
			self.session.exec_command(command)
			stdout_data = []
			while True:
				if self.session.recv_ready():
					stdout_data.append(self.session.recv(self.nbytes))
				if self.session.exit_status_ready():
					break

			return ast.literal_eval(stdout_data[0][:-1].decode("utf-8"))

	def close_session(self):
		self.session.close()
		self.client.close()
		self.session = None
		self.client = None
