import requests


def date2digits(date):
	return int("".join(date.split("-")))


def normalize(data):
	sample = data["Time Series (Daily)"]

	result = {
		"open": [],
		"high": [],
		"low": [],
		"close": [],
		"adjusted close": [],
		"volume": [],
		"dividend amount": [],
		"split coefficient": [],
		"date": [],
	}

	data_list = []

	for key in sample:  # key is a date
		data_list.append(key)

		new_key = date2digits(key)
		result["date"] = new_key

		for value in sample[key]:
			normalized_key = " ".join(value.split()[1:])
			result[normalized_key].append(float(sample[key][value]))

	return result, data_list
