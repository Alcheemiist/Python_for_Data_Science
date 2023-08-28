from matplotlib import pyplot as plt
from load_csv import load
import pandas as pd


def aff_pop_Morocco(df: pd.DataFrame, country: str = "Morocco"):
    df_morocco = df[df["country"] == country]
    df_rwanda = df[df["country"] == "Rwanda"]
    df_japan = df[df["country"] == "Japan"]
    plt.plot(df_morocco.columns[1:], df_morocco.values[0][1:], 'r--', df_japan.columns[1:], df_japan.values[0][1:], 'tab:blue', df_rwanda.columns[1:], df_rwanda.values[0][1:], 'k')
    plt.legend(['Morocco', 'Japan', 'Rwanda'], loc='lower right')
    plt.title("Morocco Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    # plt.axis([ 0, 1000,1000, 5000])
    plt.show()


def main():
    aff_pop_Morocco(load("population_total.csv"))


if __name__ == "__main__":
    main()
