class Circle (): 
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_radius(self):
        return self.radius
    def get_height(self):
        return self.height

    def calculate_area(self):
        self.area = 3.14*(self.get_radius()**2)
        return self.area
    def calculate_volume(self):
        self.volume = 3.14*(self.get_radius()**2)*self.get_height()
        return self.volume
