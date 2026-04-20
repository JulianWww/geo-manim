from ..baseConstruction import BaseConstruction
from ...geo_objects.point import Point
from ...geo_objects.line import Line
from ...geo_objects.circle import Circle
from ..intersection import LineLineIntersection, LineCircleIntersection
from .paralelLine import SeinerParalellWithCenter

class SetupHalbeisen(BaseConstruction):
    """
    Perform a steiner construction of a line through C paralel to the line AB, with O being the center of A and B
    """

    def __init__(self, A, O, C, H, hide_h = False, **kwargs):
        super(SetupHalbeisen, self).__init__(**kwargs)
        assert(isinstance(A, Point))
        assert(isinstance(H, Point))
        assert(isinstance(O, Point))
        assert(isinstance(C, Circle))
        self.A = A
        self.O = O
        self.C = C
        self.H = H
        self.hide_h = hide_h
        self.parallel = None

    def get_required_geo_objects(self):
        return [self.A, self.B, self.C, self.O, self.H].extend(super(SetupHalbeisen, self).get_required_geo_objects())

    def build_tangent(self, C, A, B, O, H):
        BH = self.ephemeral(Line(B, H))
        AC = self.ephemeral(Line(A, C))
        self.play()

        I = self.run_construction(LineLineIntersection(BH, AC, show_point=False)).get_point()
        
        T = self.run_construction(SeinerParalellWithCenter(A, B, C, O, I, show_filter= lambda o: not(o == BH), play_at_end=False))
        self.hide_all([AC, BH])
        return T.get()

    def construct(self):
        A = self.A
        O = self.O
        H = self.H
        C = self.C

        AO = self.ephemeral(Line(A, O))

        self.play()

        B = self.run_construction(LineCircleIntersection(AO, C, point_filter=lambda p: p!=A)).get_points()[0]

        AH = self.ephemeral(Line(A, H))
        I = self.run_construction(LineCircleIntersection(AH, C, show_point=lambda p: False, point_filter=lambda p: p != A)).get_points()[0]

        self.play()

        IE = self.run_construction(SeinerParalellWithCenter(A, B, I, O, H)).get()
        E = self.run_construction(LineCircleIntersection(IE, C, show_point=lambda p: False, point_filter=lambda p: p!= I)).get_points()[0]
        BE = self.ephemeral(Line(E, B))
        if (self.hide_h):
            self.hide(H)

        self.play()

        M = self.run_construction(LineLineIntersection(AH, BE, show_point=False)).get_point()
        OM = self.ephemeral(Line(M, O))
               
        self.play()
        self.hide_all([IE, BE])
        [D, U] = self.run_construction(LineCircleIntersection(OM, C, show_point=lambda p: False)).get_points()

        self.play()

        self.UPPER = self.build_tangent(U, A, B, O, I)

        self.play()

        IO = self.ephemeral(Line(I, O))

        self.play()

        self.hide(AH)
        J = self.run_construction(LineCircleIntersection(IO, C, show_point=lambda p: False, point_filter=lambda p: p!=I)).get_points()[0]
        self.LOWER = self.build_tangent(D, B, A, O, J)
        self.hide(OM)

        self.play()

        One_Tangent = self.build_tangent(A, U, D, O, J)
        self.hide(IO)

        self.play()

        self.ONE_U = self.run_construction(LineLineIntersection(One_Tangent, self.UPPER, play_at_end=False))
        self.ONE_D = self.run_construction(LineLineIntersection(One_Tangent, self.LOWER, play_at_end=False))
        self.play()
        self.hide(One_Tangent)



    
    def get(self):
        return self.parallel
        