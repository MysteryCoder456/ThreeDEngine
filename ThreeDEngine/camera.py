from glm import vec3


class Camera:
    pos = vec3(0)
    fov = 70

    @staticmethod
    def translate(vector: vec3):
        pos += vector