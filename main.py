from mmmysql.data.db_operations import Database

from mmmysql.model.location import Location
from mmmysql.model.skill import Skill
from mmmysql.model.has_skill import Has_Skill

# Este es el archivo que contiene el menú de la aplicación y que dependiendo de la opción seleccionada tomaremos una u otra acción
# Preparar los contenedores de MySql, Mongo y Neo4j  Hecho
# Insertar datos en MySql, prvia lectura de los csv_s
# 25/11/2023 Tratar de hacer los inserts de MySql


# Para docker
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "my-secret-pw"
DB_DATABASE = "dataimport"
DB_PORT = "8888"



'''
Contra fuera de docker
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_DATABASE = "wineclub"
DB_PORT = "3306"
'''

#from Models.BookStore import Bookstore
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
                    print("Carga de Mysql")
                    
                    obj = Database(DB_HOST,DB_USER,DB_PASSWORD,DB_DATABASE,DB_PORT)
                    
                    
                    
                    
                    # por cada uno que lea, que haga un insert
                    location = Location("TechHub", "Silicon Valley") 
                    #obj.insert_data2(location)
                    
                    #{"person_id": 1,"skill_id": 301, "proficiency": "Intermediate"},
                    skill = Skill("proficiency")
                    obj.insert_data3(skill)

                    
                    
                    has_skill = Has_Skill( 1, 301, "proficiency")
                    
                    #obj.insert_data4(has_skill)
                    

                    
                    
                    
                    
                    
                    '''                    
                    locations.json
                        {"id": 201,"name": "TechHub", "city": "Silicon Valley" },
                        {"id": 202, "name": "Finance Plaza","city": "New York"},
                        {"id": 203,  "name": "Manufacturing Park", "city": "Detroit" },
                        {"id": 204, "name": "Health Hub", "city": "Boston"},
                        {"id": 205, "name": "Consulting Center", "city": "Chicago" },

                    create table location(
                    id_location INT AUTO_INCREMENT PRIMARY KEY,
                    name nvarchar (10) not null,
                    city nvarchar(50) not null
                    ); 
                    '''
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
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


if __name__ == "__main__":
    main()
    

