import pandas as pd


def load(path: str) -> pd.DataFrame:
    data = open(path, "r")
    df = pd.read_csv(data)
    print("Loading dataset of dimensions", df.shape)
    return df


if __name__ == "__main__":
    print(load("life_expectancy_years.csv"))
