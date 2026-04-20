from .baseConstruction import BaseConstruction
from ..geo_objects.point import Point
from sympy.geometry import intersection

class LineLineIntersection(BaseConstruction):
    """
    Construct the intersection Point betwean L and Q 
    Giving None if they are parallel
    """
    def __init__(self, L, Q, show_point=True, **kwargs):
        super(LineLineIntersection, self).__init__(**kwargs)
        self.L = L
        self.Q = Q
        self.P = None ## the intersection Point
        self.show_point = show_point
    
    def construct(self):
        points = intersection(self.L, self.Q)
        if (len(points) == 0):
            return
        
        self.P = Point(points[0])
        
        if (self.show_point):
            self.persistent(self.P)
    
    def get_point(self):
        return self.P

class LineCircleIntersection(BaseConstruction):
    def __init__(self, L, C, show_point=lambda p: True, point_filter=lambda p: True, **kwargs):
        super(LineCircleIntersection, self).__init__(**kwargs)
        self.L = L
        self.C = C
        self.P = None ## the intersection Point
        self.show_point = show_point
        self.point_filter = point_filter
    
    def construct(self):
        points = intersection(self.L, self.C)
        if (len(points) == 0):
            return
        
        self.P = []
        
        for p in points:
            if (not self.point_filter(p)):
                continue
            
            P = Point(p)
            self.P.append(P)

            if (self.show_point(p)):
                self.persistent(P)
    
    def get_points(self,):
        return self.P