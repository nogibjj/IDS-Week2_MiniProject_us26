import pandas as pd

def stats(dataset):
    mean_val = dataset.mean(numeric_only=True)
    median_val = dataset.median(numeric_only=True)
    mode_val = dataset.mode(numeric_only=True)
    return mean_val, median_val, mode_val


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
    answers = stats(df)

