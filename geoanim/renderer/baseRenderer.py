from manim import Scene, Create, FadeOut, AnimationGroup
from .animations.animationHandler import AnimationHandler
from sympy import Polygon


class BaseRenderer(Scene):
    def __init__(self):
        super(BaseRenderer, self).__init__()
        self.animation_handler: AnimationHandler = AnimationHandler()
    
    def show_mobject(self, mobject, animation=Create, **kwargs):
        self.animation_handler.add_show_animation(animation(mobject, **kwargs))

    def hide_mobject(self, mobject, animation=FadeOut, **kwargs):
        self.animation_handler.add_hide_animation(animation(mobject, **kwargs))
    
    def show_geo_object(self, geo_object):
        geo_object.initialize(self)
        geo_object.show(self)

    def hide_geo_object(self, geo_object):
        geo_object.hide(self)

    def run_construction(self, construction):
        construction.setScene(self)
        construction.doConstruction()
        return construction

    def play(self):
        animations = self.animation_handler.get_animations()
        print(animations)
        if (len(animations) == 0):
            return
        
        super(BaseRenderer, self).play(*animations)

    def get_visible_area(self):
        return Polygon((7,4),(7,-4),(-7,-4),(-7,4))