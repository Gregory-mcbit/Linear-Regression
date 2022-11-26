import matplotlib.pyplot as plt


decoder = {
    0: "close-prediction",
    1: "open-prediction",
}


def visualize(ticker, *dataframes):
    counter = 0

    for df in dataframes:
        df.plot(kind="bar", fontsize=5)
        plt.title(ticker, fontsize=15)
        plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
        plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
        plt.savefig(f"./hists/{decoder[counter]}-dataframe.png")
        counter += 1
