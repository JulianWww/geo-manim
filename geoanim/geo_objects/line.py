from sympy.geometry.line import Line2D as SymLine
from manim import Line as Mline
from .geoObject import GeoObject
from .utils import to_point

def set_line_enpoints_to_edge(mobj, line, scene):
    visible_area = scene.get_visible_area()
    points = visible_area.intersection(line)
    if len(points) == 0:
        return None
    elif len(points) == 1:
        points.append(points[0])
    [a,b] = points
    mobj.set_points_by_ends(to_point(a), to_point(b))

class Line(GeoObject, SymLine):
    def __init__(self, *args, **kwargs):
        super(Line, self).__init__(*args, **kwargs)

    def construct(self, scene):
        super(Line, self).construct(scene)
        line = Mline()
        set_line_enpoints_to_edge(line, self, scene)
        self.add(line)