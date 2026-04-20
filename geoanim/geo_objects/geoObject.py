from ..visible_object import VisibleObject

class GeoObject(VisibleObject):    
    def initialize(self, scene):
        if (self.initialized):
            return
        super(GeoObject, self).initialize(scene)
        self.construct(scene)