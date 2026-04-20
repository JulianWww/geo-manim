from manim import AnimationGroup as AnimationSet

class AnimationGroup:
    def __init__(self):
        self.animations = []
    
    def add_animation(self, anim):
        self.animations.append(anim)
    
    def get_animations(self, animation_list):
        if (len(self.animations) != 0):
            animation_list.extend(self.animations)
        self.clear()

    def clear(self):
        self.animations.clear()