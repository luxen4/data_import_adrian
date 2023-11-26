import mysql.connector
from mmmysql.model.location import Location
from mmmysql.model.skill import Skill
from mmmysql.model.has_skill import Has_Skill
# pip install mysql-connector-python



class Database:
    def __init__(self, host, user, password, database,port):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            department VARCHAR(255)
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()



    def insert_data(self, employee):
        insert_query = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
        data = (employee.name, employee.age, employee.department)
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        #Cogemos el id de la última fila insertada
        employee_id = self.cursor.lastrowid
        return Employee(employee.name, employee.age, employee.department, employee_id)





    def get_all_data(self):
        select_all_query = "SELECT * FROM employees"
        self.cursor.execute(select_all_query)
        result = self.cursor.fetchall()
        employees = []
        for row in result:
            employee = Employee(row[1], row[2], row[3], row[0])  #Cuidado con el orden
            employees.append(employee)
        return employees

    def update_data(self, employee):
        update_query = "UPDATE employees SET name=%s, age=%s, department=%s WHERE id=%s"
        data = (employee.name, employee.age, employee.department, employee.id)
        self.cursor.execute(update_query, data)
        self.connection.commit()

    def delete_data(self, employee_id):
        delete_query = "DELETE FROM employees WHERE id=%s"
        data = (employee_id,)
        self.cursor.execute(delete_query, data)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        
        
        
        
        
        
        
        
        
        
    def insert_data2(self, location):
        insert_query = "INSERT INTO location (name, city) VALUES (%s, %s)"
        data = (location.name, location.city)
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        #Cogemos el id de la última fila insertada
        location_id = self.cursor.lastrowid
        return Location(location.name, location.city, location_id)
    
    
    def insert_data3(self, skill):
        insert_query = "INSERT INTO skill (name) VALUES (%s)"
        data = (skill.name)
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        #Cogemos el id de la última fila insertada
        skill_id = self.cursor.lastrowid
        return Skill(skill.name, skill_id)
    
    
    def insert_data4(self, has_skill):
        insert_query = "INSERT has_skill (id_person, id_skill, proficiency) VALUES (%s, %s, %s)"
        data = (has_skill.id_person, has_skill.id_skill, has_skill.proficiency)
        self.cursor.execute(insert_query, data)
        self.connection.commit()
        #Cogemos el id de la última fila insertada
        has_skill_id = self.cursor.lastrowid
        return Has_Skill(has_skill.id_person, has_skill.id_skill, has_skill.proficiency, has_skill_id)

        '''
        id_has_skill INT AUTO_INCREMENT PRIMARY KEY,
        id_person int not null,
        id_skill int not null,
        proficiency nvarchar (30) not null'''