class TickerError(Exception):
	def __init__(self, *args):
		self.message = args[0]
		self.code_error = 5


	def __str_(self):
		return f"Ошибка {self.message} (код {self.code_error})"