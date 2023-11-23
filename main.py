# Este es el archivo que contiene el menú de la aplicación y que dependiendo de la opción seleccionada tomaremos una u otra acción
# Preparar los contenedores de MySql, Mongo y Neo4j  Hecho
# Insertar datos en MySql, prvia lectura de los csv_s





#from Models.BookStore import Bookstore
def main():
    #bookstore = Bookstore()
    #bookstore.loadDataBooksFromJson()
    
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


if __name__ == "__main__":
    main()
    

