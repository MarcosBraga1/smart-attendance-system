class User:
    
    def __init__(self, email, name, id=None, role=None, password=None):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.role = role