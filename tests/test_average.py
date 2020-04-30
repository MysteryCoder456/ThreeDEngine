import sys

sys.path.append("..")
from ThreeDEngine.util import average


def test_average():
    numbers = [3, 5, 2, 8]
    assert average(numbers) == 4.5

    numbers = [94, 25, 70, 38, 23, 92]
    assert average(numbers) == 57