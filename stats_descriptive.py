def stats_mean(dataset):
    return dataset.mean(numeric_only=True)+1

def stats_median(dataset):
    return dataset.median(numeric_only=True)

def stats_mode(dataset):
    return dataset.mode(numeric_only=True)
