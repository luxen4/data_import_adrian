from mmmysql.data.db_operations import Database
from mmmongo.data.mongo_operations import MongoDBOperations
from mmneo4j.neo4j_operations import Neo4jCRUD


from mmmysql.model.location import Location
from mmmysql.model.skill import Skill
from mmmysql.model.person_skill import Person_Skill

from mmmongo.modelmongo.newProject import NewProject
from mmmongo.modelmongo.newTeam import NewTeam
from mmmongo.modelmongo.newWork_in_Team import NewWorks_in_Team

import csv
import json
import os


# Este es el archivo que contiene el menú de la aplicación y que dependiendo de la opción seleccionada tomaremos una u otra acción
# Preparar los contenedores de MySql, Mongo y Neo4j  Hecho
# Insertar datos en MySql, prvia lectura de los csv_s
# 25/11/2023 Tratar de hacer los inserts de MySql


# Para docker Mysql
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "my-secret-pw"
DB_DATABASE = "dataimport"
DB_PORT = "8889"
 


'''
Contra fuera de docker
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "wineclub"
DB_PORT = "3306"
'''




 

# Función de insertado en MongoDB
def insercionMongoDB():
    
    # Conexión a mongo
    mongo_operations = MongoDBOperations('dataimport', 'works','8889')   # funciona OK

    print(" Inserción de projects")
    # leer el csv para que empiece a meter
    filename = "./resources/MongoDB/projects.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            project = NewProject(project_id= row[0], name=row[1], description=row[2], skill_id=row[3], location_id= row[4], company_id=row[5])
            mongo_operations.create_project(project)
            
            
    # Conexión a mongo
    mongo_operations = MongoDBOperations('dataimport', 'teams','8889')   # funciona OK
            
    print(" Inserción de teams")
    # leer el csv para que empiece a meter
    filename = "./resources/MongoDB/teams.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            team = NewTeam(team_id= row[0], name=row[1], description=row[2], project_id=row[3])
            mongo_operations.create_team(team)  
            
            
        # Conexión a mongo
    mongo_operations = MongoDBOperations('dataimport', 'works_in_team','8889')   # funciona OK
            
    print(" Inserción de works_in_teams")
    # leer el csv para que empiece a meter
    filename = "./resources/MongoDB/works_in_team.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            worksInTeam = NewWorks_in_Team(person_id= row[0], team_id=row[1], role=row[2])
            mongo_operations.create_team(worksInTeam) 


def insercionMysql():
    obj = Database(DB_HOST,DB_USER,DB_PASSWORD,DB_DATABASE,DB_PORT)
    # Abre el archivo JSON y lee su contenido 
    # por cada uno que lea, que haga un insert
    with open('./resources/Data_Mysql/locations.json', 'r') as archivo_json:
        datos = json.load(archivo_json)
        
    for i in range(0, len(datos), 1):
        city=datos[i]['city']
        name=datos[i]['name']
        location = Location(city, name) 
        obj.insert_data2(location)

    # Abre el archivo JSON y lee su contenido
    with open('./resources/Data_Mysql/skills.json', 'r') as archivo_json:
        datos = json.load(archivo_json)
        
    for i in range(0, len(datos), 1):
        id=datos[i]['id']
        name=datos[i]['name']
    
        # por cada uno que lea, que haga un insert
        skill = Skill(name, id) 
        obj.insert_data3(skill)
    
    # Abre el archivo JSON y lee su contenido
    with open('./resources/Data_Mysql/personSkill.json', 'r') as archivo_json:
        datos = json.load(archivo_json)
        
    for i in range(0, len(datos), 1):
        person_id=datos[i]['person_id']
        skill_id=datos[i]['skill_id']
        proficiency=datos[i]['proficiency']
    
        # por cada uno que lea, que haga un insert
        person_skill = Person_Skill(person_id, skill_id, proficiency) 
        obj.insert_data4(person_skill)











def main():
    #bookstore = Bookstore()
    #bookstore.loadDataBooksFromJson()
    '''  
    while True:
        choice = int(input("Enter your choice: "))
        print("0. Carga de datos.")
        print("1. Personas y sus roles en una empresa concreta.")
        print("2. Personas con el mismo rol en diferentes empresas.")
        print("3. Empresas comunes entre dos personas.")
        print("4. Personas y sus funciones en un equipo específico.")
        print("5. Muestra todos los equipos con el número de personas que los componen.")
        print("6. Muestra los equipos con el número total de proyectos a los que están asociados.")
        print("7. Obtener todas las skills en las que una persona tiene al menos un nivel específico de proficiency")
        print("8. Encontrar todas las personas que tienen skill en al menos una skill en común con otra persona (es decir, encontrar personas con skills similares).")
        print("9. Dado una ubicación, obtén la lista de equipos que están ubicados allí junto con información de las personas que trabajan en ese equipo y los proyectos asociados.")
        print("10. EXit.")

        try:
            match choice:
                case 1:
                    print("")
                case 2:
                    print("")
                case 3:
                    print("")
                case 4:
                    print("")
                case 5:
                    print("")
                case 6:
                    print("")
                case 7:
                    print("")
                case 8:
                    print("")
                case 9:
                    print("")
                case 10:
                    print("Goodbye!")
                    break
                case _:
                    
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")
        '''



    while True:
        choice = int(input("Enter your choice: "))
        
        print("1. Neo4j_persons.csv.")
        print("2. Neo4j_empresas.csv")
        print("3. Neo4j_works_at.csv.")
        
        print("4. MySql_locations.json.")
        print("5. MySql_skills.json.")
        print("6. MySql_has_skill.json")
        
        print("7. Mongo_projects.csv")
        print("8. Mongo_teams.csv")
        print("9. Mongo_works_in_team.csv")
        
        print("10. EXIT carga de datos")

        try:
            match choice:
                case 1:
                    print("")
                    
                    
                    
                    
                    
                case 2:
                    print("")
                case 3:
                    print("")
                case 4:
                    print("Inserción en MySql")
                    insercionMysql()
                case 5:
                    print("Inserción en MongoDB")
                    insercionMongoDB()
                    
                case 6:
                    print("Inserción Neo4j")
                    
                    # Conexión a neo4j
                    uri = "bolt://localhost:7687"  
                    user = "neo4j"
                    password = "alberite"
                    neo4j_crud = Neo4jCRUD(uri, user, password)
                    
                    print(" Inserción de companies")
                    filename = "./resources/Data_Neo4j/companies.csv"
                    with open(filename, 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            print(row)
                            id=row[0]
                            name=row[1]
                            industry=row[2]
                            
                            # Example: Create a node
                            node_properties = {"id":id, "name":name, "industry":industry }
                            created_node = neo4j_crud.create_node("Companies", node_properties)
                            #print(f"Created Node: {created_node}")
                            
                    print(" Inserción de persons")
                    filename = "./resources/Data_Neo4j/persons.csv"
                    with open(filename, 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            print(row)
                            id=row[0]
                            name=row[1]
                            age=row[2]
                            
                            # Example: Create a node
                            node_properties = {"id":id, "name":name, "age":age }
                            created_node = neo4j_crud.create_node("Persons", node_properties)
                            print(f"Created Node: {created_node}")
                            
                    print(" Inserción de works_at")
                    filename = "./resources/Data_Neo4j/works_at.csv"
                    with open(filename, 'r') as file:                  
                        reader = csv.reader(file)
                        iterator = iter(reader)
                        next(iterator)
                        for row in iterator:
                            print(row)
                            person_id=row[0]
                            company_id=row[1]
                            role=row[2]
                            location_id=row[3]
                            
                            # Example: Create a node
                            node_properties = {"person_id":person_id, "company_id":company_id, "role":role, "location_id":location_id }
                            neo4j_crud.create_relationshipAdrian2("Persons","Companies","Works_at",node_properties)  
                    
                case 7:
                    print("")
                case 8:
                    print("")
                case 9:
                    print("")
                case 10:
                    print("Goodbye!")
                    break
                case _:
                    
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
