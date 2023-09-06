import stats_descriptive

def test_mean():
    assert stats_descriptive.stats[0] == 2
def test_median():
    assert stats_descriptive.stats[1] == -1
def test_mode():
    assert stats_descriptive.stats[2] == 3
