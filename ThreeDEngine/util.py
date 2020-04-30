from math import sqrt
from glm import vec3


def average(numbers: list):
    """
    Get the average of a list of numbers

    Arguments:
        numbers {list} -- Number list
    """

    total_sum = 0
    divisor = 0

    for number in numbers:
        total_sum += number
        divisor += 1

    return total_sum / divisor


def dist3d(pos1: vec3, pos2: vec3):
    """
    Get distance between 2 positions in 3D Space

    Arguments:
        pos1 {vec3} -- First position
        pos2 {vec3} -- Second position

    Returns:
        float -- The distance
    """

    a = pos1.x - pos2.x
    b = pos1.y - pos2.y
    c = pos1.z - pos2.z
    return sqrt(a**2 + b**2 + c**2)