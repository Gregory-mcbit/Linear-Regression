from . import ticker_error
from . import settings
import requests


def get_url(ticker=None, function="TIME_SERIES_DAILY_ADJUSTED"):
	if ticker is None:
		error = ticker_error.TickerError("Тикер не был указан")
		return error, False

	api_key = settings.settings["api_key"]

	url = f"https://www.alphavantage.co/query?function={function}&symbol={ticker}&outputsize=full&apikey={api_key}"

	response = requests.get(url)
	
	if response.status_code == 200:
		if response.json().get("Error Message"):
			error = ticker_error.TickerError("Тикер не был найден. Попробуйте заново")

			return error, False

		return url, True

	return "Ошибка соединения (код {response.status_code})", False
