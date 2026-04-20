from geoanim import *
from sympy import sqrt

class Main(BaseRenderer):
    interactive_mode = False
    
    def construct(self):
        a = Point(1,0)
        o = Point(-1, 0)

        h = Point(-3, 2.5)

        c = Circle(o, 2)

        txt = TextOverlay("Test Text")


        self.show_geo_object(a)
        self.show_geo_object(c)
        self.show_geo_object(h)
        self.show_geo_object(o)
        self.show_geo_object(txt)
        self.play()

        #self.run_construction(SetupHalbeisen(a, o, c, h, hide_h=True, play_at_end=True))

        self.hide_geo_object(a)
        self.hide_geo_object(c)
        self.hide_geo_object(o)

        self.play()


if __name__ == "__main__":
    Main()
