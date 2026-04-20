from .animationGroup import AnimationGroup

class AnimationHandler:
    def __init__(self):
        self.show_animations = AnimationGroup()
        self.hide_animations = AnimationGroup()
    
    def add_show_animation(self, anim):
        self.show_animations.add_animation(anim)
    
    def add_hide_animation(self, anim):
        self.hide_animations.add_animation(anim)
    
    def get_animations(self):
        anims = []
        self.show_animations.get_animations(anims)
        self.hide_animations.get_animations(anims)
        return anims