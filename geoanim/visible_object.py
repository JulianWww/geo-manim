from manim import Create, FadeOut

class VisibleObject:
    initialized = False
    visible = False

    def __init__(self, *args, **kwargs):
        pass
    
    def initialize(self, scene):
        if (self.initialized):
            return
        self.initialized = True
        self.mobjects = []
        self.construct(scene)
    
    def construct(self, scene):
        pass

    def add(self, mobject):
        self.mobjects.append(mobject)

    def show(self, renderer):
        if (self.visible):
            return
        assert(self.initialized)
        self.add_objects(renderer)
        self.visible = True

    def hide(self, renderer):
        if (not self.visible):
            return
        assert(self.initialized)
        self.remove_objects(renderer)
        self.visible = False
    
    def remove_objects(self, renderer):
        for idx, mobject in enumerate(self.mobjects):
            renderer.hide_mobject(mobject, self.hide_anim(idx, mobject))
    
    def clear(self, renderer):
        self.remove_objects(renderer)
        self.mobjects.clear()
    
    def add_objects(self, renderer):
        for idx, mobject in enumerate(self.mobjects):
            renderer.show_mobject(mobject, self.show_anim(idx, mobject))
        
    def show_anim(self, idx, mobj):
        return Create
    
    def hide_anim(self, idx, mobj):
        return FadeOut