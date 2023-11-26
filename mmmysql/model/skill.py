# Aquí haremos un objeto que después se lo meteremos al insert por medio de sus atributos
class Skill:
    def __init__(self, name, skill_id=None):
        self.id = skill_id
        self.name = name
        
    
    def __str__(self):
        return f'id: {self.id}, name: {self.name}'