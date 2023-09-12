from stats_descriptive import (
    stats_mean,
    stats_median,
    stats_mode,
    stats_std,
    report,
    create_summary,
)
import pandas as pd

data = pd.read_csv("World University Rankings 2023.csv")

# Calculating values for "No of student per staff"


def test_values():
    assert (stats_mean(data)) == 16.724999999999998
    assert (stats_median(data)) == 13.5
    assert (stats_mode(data)[0]) == 10.3
    assert (stats_std(data)) == 10.557828968365254


test_values()
create_summary(data, file_path="Generated summary report.md")
