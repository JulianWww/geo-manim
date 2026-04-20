from sympy.geometry import Point2D
from .geoObject import GeoObject
from manim import Dot
from .utils import to_point

class Point(GeoObject, Point2D):
    def __init__(self, *args, **kwargs):
        super(Point, self).__init__(*args, **kwargs)
    
    def construct(self, scene):
        super(Point, self).construct(scene)
        P = Dot()
        P.move_to(to_point(self))
        self.add(P)