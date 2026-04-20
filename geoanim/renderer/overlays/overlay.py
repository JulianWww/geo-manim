from ...visible_object import VisibleObject
from manim import Tex, BackgroundRectangle, Write, Unwrite

class TextOverlay(VisibleObject):  
    def __init__(self, text):
        super(TextOverlay, self).__init__()
        self.text = text

    def construct(self, scene):
        for obj in self.get_text_object(self.text):
            self.add(obj)
    
    def set_text(self, text):
        self.text = text

    def get_text_object(self, text):
        tex = Tex(text)
        rec = BackgroundRectangle(tex, color="black", buff=0.1, fill_opacity=1)
        return [rec, tex]

    def show_anim(self, idx, mobj):
        if (idx == 1):
            return Write
        return super(TextOverlay, self).show_anim(idx, mobj)
    
    def hide_anim(self, idx, mobj):
        return Unwrite