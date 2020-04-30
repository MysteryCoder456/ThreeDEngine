import sys
from glm import vec3

sys.path.append("..")
from ThreeDEngine.util import dist3d


def test_dist3d():
    pos1 = vec3(500, 500, 500)
    pos2 = vec3(500, 500, 600)
    assert dist3d(pos1, pos2) == 100

    pos1 = vec3(300, 100, 400)
    pos2 = vec3(600, 100, 800)
    assert dist3d(pos1, pos2) == 500