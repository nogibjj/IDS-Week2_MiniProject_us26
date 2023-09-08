from  stats_descriptive import stats_mean ,  stats_median ,  stats_mode
import pandas as pd

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

def test_values():
    assert (stats_mean(df)[0]) == 13.083333333333334
    assert (stats_median(df)[0]) == 14.0
    assert (stats_mode(df)["Age"][0]) == 15
