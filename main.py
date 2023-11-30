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


# Conexión a neo4j
uriNeo4j = "bolt://localhost:7687"  
userNeo4j = "neo4j"
passwordNeo4j = "alberite"
neo4j_crud = Neo4jCRUD(uriNeo4j, userNeo4j, passwordNeo4j)



# Para docker Mysql
'''
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "my-secret-pw"
DB_DATABASE = "dataimport"
DB_PORT = "8888"
'''


'''
Contra fuera de docker
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "wineclub"
DB_PORT = "3306"
'''

dabaseMongo="dataimport"
portMongo="8889"


DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "my-secret-pw"
DB_DATABASE = "dataimport"
DB_PORT = "8888"






# Función que carga los registros en MongoDB
def insercionMongoDB():
    
    # Conexión a mongo
    mongo_operations = MongoDBOperations(dabaseMongo, 'works',portMongo)   # funciona OK

    print(" Inserción de projects")
    # leer el csv para que empiece a meter
    filename = "./resources/MongoDB/projects.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            project = NewProject(project_id= row[0], name=row[1], description=row[2], skill_id=row[3], location_id= row[4], company_id=row[5])
            mongo_operations.create_project(project)
            
            
    # Conexión a mongo
    mongo_operations = MongoDBOperations(dabaseMongo, 'teams',portMongo)   # funciona OK
            
    print(" Inserción de teams")
    # leer el csv para que empiece a meter
    filename = "./resources/MongoDB/teams.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            team = NewTeam(team_id= row[0], name=row[1], description=row[2], project_id=row[3])
            mongo_operations.create_team(team)  
            
            
        # Conexión a mongo
    mongo_operations = MongoDBOperations(dabaseMongo, 'works_in_team',portMongo)   # funciona OK
            
    print(" Inserción de works_in_teams")
    # leer el csv para que empiece a meter
    filename = "./resources/MongoDB/works_in_team.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            worksInTeam = NewWorks_in_Team(person_id= row[0], team_id=row[1], role=row[2])
            mongo_operations.create_team(worksInTeam) 

# Función que carga los registros en Mysql
def insercionMysql():
    try:
        obj = Database(DB_HOST,DB_USER,DB_PASSWORD,DB_DATABASE,DB_PORT)
    except Exception as ex :
        print(ex)
        
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
        
# Función que carga los registros en neo4j
def insercionNeo4j():
    
    print(" Inserción de companies")
    filename = "./resources/Data_Neo4j/companies.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            id=row[0]
            name=row[1]
            industry=row[2]
            
            node_properties = {"id":id, "name":name, "industry":industry }
            created_node = neo4j_crud.create_node("Companies", node_properties)
            #print(f"Created Node: {created_node}")
            
    print(" Inserción de persons")
    filename = "./resources/Data_Neo4j/persons.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            id=row[0]
            name=row[1]
            age=row[2]
            
            node_properties = {"id":id, "name":name, "age":age }
            created_node = neo4j_crud.create_node("Persons", node_properties)
            #print(f"Created Node: {created_node}")
            
    print(" Inserción de works_at")
    filename = "./resources/Data_Neo4j/works_at.csv"
    with open(filename, 'r') as file:                  
        reader = csv.reader(file)
        iterator = iter(reader)
        next(iterator)
        for row in iterator:
            person_id=row[0]
            company_id=row[1]
            role=row[2]
            location_id=row[3]
            
            node_properties = {"person_id":person_id, "company_id":company_id, "role":role, "location_id":location_id }
            neo4j_crud.create_relationshipAdrian2("Persons","Companies","Works_at",node_properties) 


def cargaDatos():
    print("Inserción en MySql")
    insercionMysql()

    #print("Inserción en MongoDB")
    #insercionMongoDB()

    #print("Inserción en MongoDB")
    #insercionNeo4j()



def main(): 
    while True:
        choice = int(input("Enter your choice: "))
        print("0. Carga de datos.")
        print("1. Personas y sus roles en una empresa concreta.")################ Neo4j
        print("2. Personas con el mismo rol en diferentes empresas.")
        
        
        
        print("3. Empresas comunes entre dos personas.")#########################
        print("4. Personas y sus funciones en un equipo específico.") 
        
        print("5. Muestra todos los equipos con el número de personas que los componen.")
        
        
        print("6. Muestra los equipos con el número total de proyectos a los que están asociados.")
        print("7. Obtener todas las skills en las que una persona tiene al menos un nivel específico de proficiency")
        print("8. Encontrar todas las personas que tienen skill en al menos una skill en común con otra persona (es decir, encontrar personas con skills similares).")
        print("9. Dado una ubicación, obtén la lista de equipos que están ubicados allí junto con información de las personas que trabajan en ese equipo y los proyectos asociados.")
        print("10. EXit.")

        try:
            match choice:
                case 0:
                    cargaDatos()
                    
                case 1:
                    query = "MATCH (p:Persons)-[w:Works_at]-(c:Companies {name:'ABC Corp' }) RETURN p.name, w.role, c.name"
                    results = neo4j_crud.run_query(query)
                    for i in range (0 ,len(results),1):
                        dic=results[0]
                        
                        print(dic['p.name'] + " is an " + dic['w.role'], "en la empresa: '" + dic['c.name'] + "'" )
                       
                    
                    
                    
                case 2: 
                    # 2. Personas con el mismo rol en diferentes empresas." RAFA OK  Yvone(Pilot) con Alpha Airlines y Robo Robers
                    query = (
                    f" MATCH (c:Companies)-[w2:Works_at]-(p:Persons),"
                    f"       (c1:Companies)-[w:Works_at]-(p2:Persons) "
                    f"       where w2.role = w.role and c.name <> c1.name and p.id = p2.id "
                    f"       return p.name, w.role, c.name" )
                        
                    results = neo4j_crud.run_query(query)
                    for i in range (0 ,len(results),1):
                        dic=results[i]
                        print(dic['p.name'] + " is an " + dic['w.role'], "en la empresa: '" + dic['c.name'] + "'" )
 
                case 3: # OK 3. Empresas comunes entre dos personas."
                    
                    query = (
                    f"MATCH (c:Companies)-[w2:Works_at]-(p:Persons),"
                    f"      (c1:Companies)-[w:Works_at]-(p2:Persons) "
                    f"      where c.name = c1.name and p.id <> p2.id "
                    f"      return p.id, p.name, w.company_id ,c.name" )
                   
                   
                    results = neo4j_crud.run_query(query)
                    for i in range (0 ,len(results),1):
                        dic=results[i]
                        print(dic['p.id'] + "-" + dic['p.name'] + "-   " + dic['w.company_id'], "-'" + dic['c.name'] + "'" )
                        
                case 5: # OK 5. Muestra todos los equipos con el número de personas que los componen."
                    print("Cuidado que salen 4, que lo he trucado el csv")
                    

                    
                    lookup={"from": 'teams', "localField": 'team_id', "foreignField": 'team_id', "as": 'info'}
                    
                     # Example aggregation pipeline
                    pipeline = [
                        {"$lookup": lookup},
                        {"$unwind":'$info'},
                        {"$group": {"_id": "$info.name", "total_persons": {"$sum": 1}}},
                        {"$project": {"_id": 1 , "total_persons": 1 }} 
                    ]
                    
                    
                    # Example aggregation pipeline
                    #pipeline = [
                    #    {"$group": {"_id": "$department", "averageAge": {"$avg": "$age"}}},
                    #    {"$sort": {"averageAge": -1}}
                    #]
                                        
                    
                    mongo_operations = MongoDBOperations(dabaseMongo, 'works_in_team',portMongo)   # funciona OK run_aggregation
                    lista = mongo_operations.run_aggregation(pipeline)
                    #print (lista)
                    
                    
                    for list in lista:
                        print( str(list['total_persons']) + " personas en " + list['_id']  )

                    
                    
                case 6:
                    # 6. Casi ---Muestra los equipos con el número total de proyectos a los que están asociados.
                    '''
                    db.teams.aggregate(
                    {$lookup: {from: 'projects', localField: "project_id", foreignField: "project_id", as: 'info'}},
                    {$group: {_id: "$project_id", total_proyectos: {"$sum": 1},  "nombre_equipo": {"$first": "$name"}}},
                    {$sort: {total_proyectos: -1}},
                    {$project: { _id: 0 , nombre_equipo:1, total_proyectos: 1 }}
                    );'''
                    
                    lookup={"from": 'projects', "localField": 'project_id', "foreignField": 'project_id', "as": 'info'}
                    
                     # Example aggregation pipeline
                    pipeline = [
                        {"$lookup": lookup},
                        {"$unwind":'$info'},
                        {"$group": {"_id": "$project_id", "total_proyectos": {"$sum": 1}, "nombre_equipo": {"$first": "$name"}}},
                        {"$project": {"_id": 0 , "nombre_equipo":1, "total_proyectos": 1  }} 
                    ]
                    
                    
                    mongo_operations = MongoDBOperations(dabaseMongo, 'teams',portMongo)   # funciona OK run_aggregation
                    lista = mongo_operations.run_aggregation(pipeline)
                    #print (lista)
                    
                    
                    for list in lista:
                        print( str(list['total_proyectos']) + " proyectos en " + list['nombre_equipo']  )


                    
                    
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
