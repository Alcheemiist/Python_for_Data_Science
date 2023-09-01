from matplotlib import pyplot as plt
from load_csv import load
import pandas as pd


def aff_pop_Morocco(df: pd.DataFrame, country: str = "Morocco"):
    df_morocco = df[df["country"] == country].loc[:, '1800':'2050']
    df_rwanda = df[df["country"] == "Rwanda"].loc[:, '1800':'2050']
    df_japan = df[df["country"] == "Japan"].loc[:, '1800':'2050']
    plt.figure(figsize=(12, 6))
    plt.plot(df_morocco.columns[1:], df_morocco.values[0][1:], 'r--', df_japan.columns[1:], df_japan.values[0][1:], 'tab:blue', df_rwanda.columns[1:], df_rwanda.values[0][1:], 'k')
    plt.legend(['Morocco', 'Japan', 'Rwanda'], loc='lower right')
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(df_morocco.columns[::40])
    plt.yticks(df_morocco.values[0][::1000000])
    plt.show()


def main():
    aff_pop_Morocco(load("population_total.csv"))


if __name__ == "__main__":
    main()
