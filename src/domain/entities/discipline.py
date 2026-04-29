class DisciplineModel:
    
    def __init__(self, name, code, semester, professor, id = None):
        self.id = id
        self.name = name
        self.code = code
        self.semester = semester
        self.professor = professor