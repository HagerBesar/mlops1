from sum import sum_xy

def test_sum():
    assert 4 == sum_xy(1,3)
    assert 5 == sum_xy(2,3)
    assert 8 == sum_xy(4,4)

