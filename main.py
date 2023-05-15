from scripts import get_data, url_error, settings, predictor, visualize, custom_prediction_metric
import os
from random import randint


def main():
    ticker = input("Введите тикер. (Пример - AAPL) -> ").upper()

    url, status_ok = get_data.get_url(ticker)

    if status_ok:
        settings.settings["url"] = url

        predicted_close_dataframe, predicted_open_dataframe = predictor.predict(url, example=False)

        # visualize 5 (recommended) random predictions from each dataframe
        delta = int(input("Укажите количество отображаемых предсказаний (рекомендуется 5) -> "))
        digit = randint(0, len(predicted_close_dataframe))
        visualize.visualize(ticker, predicted_close_dataframe[digit:digit + delta],
                            predicted_open_dataframe[digit:digit + delta])

        # custom metric to show percentage of right prediction. for additional description see class annotation
        close_prediction_accuracy = custom_prediction_metric.CustomAccuracy(
            predicted_close_dataframe,
            delta=0.01,
            number_of_decimal_places=4
        )
        close_accuracy = close_prediction_accuracy.calculate()
        close_accuracy_in_percents = close_prediction_accuracy.calculate_percentages()

        open_prediction_accuracy = custom_prediction_metric.CustomAccuracy(
            predicted_open_dataframe,
            delta=0.01,
            number_of_decimal_places=4
        )
        open_accuracy = open_prediction_accuracy.calculate()
        open_accuracy_in_percents = open_prediction_accuracy.calculate_percentages()

        return f"\n\nУспех! Гистограммы, показывающие точность предсказаний, находятся в папке hists\nТочность " \
               f"предсказания цены закрытия в процентах: {close_accuracy_in_percents}\nТочность предсказания цены " \
               f"открытия в процентах: {open_accuracy_in_percents}. "

    else:
        error = url_error.UrlError("Ошибка соединения")
        return error


if __name__ == "__main__":
    print(main())
