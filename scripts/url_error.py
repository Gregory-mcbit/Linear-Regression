class UrlError(Exception):
	def __init__(self, *args):
		self.message = args[0]
		self.code_error = 6


	def __repr_(self):
		return f"Ошибка {self.message} (код {self.code_error})"