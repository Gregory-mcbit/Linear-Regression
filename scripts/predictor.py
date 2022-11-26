import requests
from . import settings
from . import normalize
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


def predict(url, example=False, example_url=None):
    if example_url:
        url = example_url

    r = requests.get(url)
    data = r.json()

    data, data_list = normalize.normalize(data)

    dataset = pd.DataFrame(data, index=data_list)

    if example:
        return dataset

    # close data contains close prices. open data the opposite - open prices
    close_data = dataset.iloc[:, 3]
    open_data = dataset.iloc[:, 0]

    # to predict close price, we need open price. same with open price
    # in dataset_with_closed we have close price to predict open price
    # in dataset_with_opened we have open price to predict close price
    dataset_with_closed, dataset_with_opened = dataset.drop("open", axis=1), dataset.drop("close", axis=1)

    # splitting to train and test data to predict open price
    x_train_open, x_test_open, y_train_open, y_test_open = train_test_split(
        dataset_with_closed,
        open_data,
        test_size=0.20,
        random_state=False
    )

    # splitting to train and test data to predict close price
    x_train_close, x_test_close, y_train_close, y_test_close = train_test_split(
        dataset_with_opened,
        close_data,
        test_size=0.20,
        random_state=False
    )

    # linear regression for close price
    regressor_close = LinearRegression()
    regressor_close.fit(x_train_close, y_train_close)

    # predicting close price
    close_predict = regressor_close.predict(x_test_close)
    predicted_close_dataframe = pd.DataFrame({"Actual": y_test_close, "Prediction": close_predict})

    # MSE for close prediction
    mse_closed = f"Mean squared error: {metrics.mean_squared_error(y_test_close, close_predict)}"
    settings.settings["mse_closed"] = mse_closed

    # MAE for close prediction
    mae_close = f"Mean squared error: {metrics.mean_squared_error(y_test_close, close_predict)}"
    settings.settings["mae_close"] = mae_close

    # linear regression for open price
    regressor_open = LinearRegression()
    regressor_open.fit(x_train_open, y_train_open)

    # predicting open price
    open_predict = regressor_open.predict(x_test_open)
    predicted_open_dataframe = pd.DataFrame({"Actual": y_test_open, "Prediction": open_predict})

    # MSE for open prediction
    mse_opened = f"Mean squared error: {metrics.mean_squared_error(y_test_open, open_predict)}"
    settings.settings["mse_opened"] = mse_opened

    # MAE for open prediction
    mae_opened = f"Mean squared error: {metrics.mean_squared_error(y_test_open, open_predict)}"
    settings.settings["mae_opened"] = mae_opened

    return predicted_close_dataframe, predicted_open_dataframe
