class Student:
    
    def __init__(self, user, registration, course, id = None):
        self.id = id
        self.user = user
        self.registration = registration
        self.course = course