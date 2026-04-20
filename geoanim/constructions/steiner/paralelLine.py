from ..baseConstruction import BaseConstruction
from ...geo_objects.point import Point
from ...geo_objects.line import Line
from ..intersection import LineLineIntersection

class SeinerParalellWithCenter(BaseConstruction):
    """
    Perform a steiner construction of a line through C paralel to the line AB, with O being the center of A and B, with helper point H on the line AC, not A or C
    """

    def __init__(self, A, B, C, O, H=None, **kwargs):
        super(SeinerParalellWithCenter, self).__init__(**kwargs)
        assert(isinstance(A, Point))
        assert(isinstance(B, Point))
        assert(isinstance(C, Point))
        assert(isinstance(O, Point))
        self.A = A
        self.B = B
        self.C = C  
        self.O = O
        self.H = H
        self.parallel = None

    def get_required_geo_objects(self):
        res = [self.A, self.B, self.C, self.O].extend(super(SeinerParalellWithCenter, self).get_required_geo_objects())
        if not self.H is None:
            res.append(self.H)
        return res
    
    def get_helper_point(self):
        if not self.H is None:
            # TODO assert H is valid helper point
            return self.H
        dist = 0.5
        return self.ephemeral(Point(self.C + (self.C - self.A)*dist))


    def construct(self):
        A = self.A
        B = self.B
        C = self.C
        O = self.O


        #AC = self.ephemeral(Line(A, C))
        BC = self.ephemeral(Line(B, C))

        self.play()

        H = self.get_helper_point()

        self.play()

        OH = self.ephemeral(Line(O, H))

        self.play()

        BH = self.ephemeral(Line(B, H))
        
        T = self.run_construction(LineLineIntersection(OH, BC, show_point=False, play_at_end=False)).get_point()
        AT = self.ephemeral(Line(A, T))

        

        self.play()

        D = self.run_construction(LineLineIntersection(BH, AT, show_point=False, play_at_end=False)).get_point()
        self.parallel = self.persistent(Line(C, D))
        self.hide_all([OH, BC])
        self.play()
    
    def get(self):
        return self.parallel
        