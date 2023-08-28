from matplotlib import pyplot as plt
from load_csv import load
import pandas as pd


def aff_life_Morocco(df: pd.DataFrame, country: str = "Morocco"):
    df = df[df["country"] == country]
    plt.plot(df.columns[1:], df.values[0][1:])
    plt.title("Morocco Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


def main():
    aff_life_Morocco(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
