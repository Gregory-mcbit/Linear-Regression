# def custom_accuracy(dataframe, delta=0.01) -> float:
#     """ Counts accuracy of prediction. delta is permissible error (delta * 100)% """
#
#     right_predicted = 0
#     predicted, actual = dataframe["Prediction"], dataframe["Actual"]
#
#     for index in range(len(dataframe)):
#
#         delta_in_price = actual[index] * delta
#         gap = abs((actual[index] + delta_in_price) - (actual[index] - delta_in_price))
#
#         if abs(predicted[index] - actual[index]) < gap:
#             right_predicted += 1
#
#     return right_predicted / len(dataframe)


class CustomAccuracy:
    """ Counts accuracy of prediction. delta is permissible error (delta * 100)% """

    def __init__(self, dataframe, delta=0.01, number_of_decimal_places="3"):
        self.dataframe = dataframe
        self.right_predicted = 0
        self.amount = len(self.dataframe)
        self.predicted = self.dataframe["Prediction"]
        self.actual = self.dataframe["Actual"]
        self.delta = delta
        self.number_of_decimal_places = str(number_of_decimal_places)
        self.accuracy = 0

    def calculate(self) -> float:
        for index in range(self.amount):
            delta_in_price = self.actual[index] * self.delta

            gap = abs((self.actual[index] + delta_in_price) - (self.actual[index] - delta_in_price))

            if abs(self.predicted[index] - self.actual[index]) < gap:
                self.right_predicted += 1

        self.accuracy = float(f"{self.right_predicted / len(self.dataframe) : .{self.number_of_decimal_places}}")
        return self.accuracy

    def calculate_percentages(self) -> int:
        if self.accuracy == 0:
            self.accuracy = calculate()
        return self.accuracy * 100
