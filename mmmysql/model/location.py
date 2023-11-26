# Aquí haremos un objeto que después se lo meteremos al insert por medio de sus atributos
class Location:
    def __init__(self, name, city, location_id=None):
        self.id = location_id
        self.name = name
        self.city = city
    
    def __str__(self):
        return f'id: {self.id}, name: {self.name}, city: {self.city}'