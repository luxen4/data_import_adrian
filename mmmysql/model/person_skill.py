# Aquí haremos un objeto que después se lo meteremos al insert por medio de sus atributos
class Person_Skill:
    def __init__(self, person_id , skill_id, proficiency, person_skill_id=None):
        self.id = person_skill_id
        self.person_id = person_id
        self.skill_id = skill_id
        self.proficiency = proficiency
    
    def __str__(self):
        return f'id: {self.id}, id_person: {self.person_id}, id_skill: {self.skill_id}, proficiency: {self.proficiency}'
    