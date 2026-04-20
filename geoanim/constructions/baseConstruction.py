

class BaseConstruction:
    def __init__(self, play_at_end=True, show_filter=lambda o: True):
        self.scene = None
        self.constructed = False
        self.ephemerals = []
        self.play_at_end = play_at_end
        self.show_filter = show_filter

    def setScene(self, scene):
        self.scene = scene

    def doConstruction(self):
        assert(self.scene != None)
        self.construct()

        self.constructed = True
        self.clear_ephemerals()

        if self.play_at_end:
            self.play()
    
    def construct(self):
        pass

    def persistent(self, geo_object):
        self.show(geo_object)
        return geo_object

    def ephemeral(self, geo_object):
        self.ephemerals.append(geo_object)
        return self.persistent(geo_object)

    def hide(self, geo_object):
        self.scene.hide_geo_object(geo_object)
    
    def hide_all(self, geo_objects):
        for obj in geo_objects:
            self.hide(obj)

    def show(self, geo_object):
        if (self.show_filter(geo_object)):
            self.scene.show_geo_object(geo_object)
    
    def show_all(self, geo_objects):
        for obj in geo_objects:
            self.show(obj)
    
    def clear_ephemerals(self):
        self.hide_all(self.ephemerals)
    
    def play(self):
        self.scene.play()
    
    def run_construction(self, construction):
        return self.scene.run_construction(construction)

    def get_required_geo_objects(self):
        return []