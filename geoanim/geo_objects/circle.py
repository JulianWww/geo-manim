from sympy.geometry import Circle as SymCirc
from .geoObject import GeoObject
from manim import Circle as ManimCirc
from .utils import to_point

class Circle(GeoObject, SymCirc):
    def __init__(self, *args, **kwargs):
        super(Circle, self).__init__(*args, **kwargs)
    
    def construct(self, scene):
        super(Circle, self).construct(scene)
        C = ManimCirc(self.radius)
        C.move_to(to_point(self.center))
        self.add(C)