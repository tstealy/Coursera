
class FileReader:
	def __init__(self, filepath):
		self.filepath = filepath
	def read(self):
		try:
			with open(self.filepath, 'r') as r:
				return r.read()
		except IOError:
			return ""



