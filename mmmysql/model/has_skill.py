# Aquí haremos un objeto que después se lo meteremos al insert por medio de sus atributos
class Has_Skill:
    def __init__(self, id_person ,id_skill, proficiency, has_skill_id=None):
        self.id = has_skill_id
        self.id_person = id_person
        self.id_skill = id_skill
        self.proficiency = proficiency
    
    def __str__(self):
        return f'id: {self.id}, id_person: {self.id_person}, id_skill: {self.id_skill}, proficiency: {self.proficiency}'
    