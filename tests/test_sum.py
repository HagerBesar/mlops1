import sys
sys.path.append('E:\1-AI_Iti\MLOPS\Task1\mlopsT1\sum.py')
from sum import sum_xy

def test_sum():
    assert 4 == sum_xy(1,3)
    assert 5 == sum_xy(2,3)
    assert 8 == sum_xy(4,4)
    assert 6 == sum_xy(2,4)

