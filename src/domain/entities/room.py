class RoomModel:
    
    def __init__(self, name, building, latitude, longitude, allowed_radius, id=None):
        self.id = id
        self.name = name
        self.building = building
        self.latitude = latitude
        self.longitude = longitude
        self.allowed_radius = allowed_radius