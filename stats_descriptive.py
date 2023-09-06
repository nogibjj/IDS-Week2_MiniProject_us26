import pandas as pd

def stats_mean(dataset):
    return dataset.mean(numeric_only=True)

def stats_median(dataset):
    return dataset.median(numeric_only=True)

def stats_mode(dataset):
    return dataset.mode(numeric_only=True)

data = [
    ["tom", 10],
    ["nick", 15],
    ["juli", 14],
    ["Faizan", 10],
    ["John", 15],
    ["Kyran", 14],
    ["Francis", 10],
    ["Diego", 15],
    ["Asad", 14],
    ["Ollie", 10],
    ["Rafael", 15],
    ["Cecil", 15],
]

df = pd.DataFrame(data, columns=["Name", "Age"])

if __name__ == "__main__":
    (stats_mean(df)[0])
    (stats_median(df)[0])
    (stats_mode(df)["Age"][0])
