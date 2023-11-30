from mmmysql.data.db_operations import Database
from mmmongo.modelmongo.newWork_in_Team import NewWorks_in_Team	
from mmmysql.model.location import Location

import csv	
import json
import os	


DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "my-secret-pw"
DB_DATABASE = "dataimport"
DB_PORT = "8889"

print("entro")

obj = Database(DB_HOST,DB_USER,DB_PASSWORD,DB_DATABASE,DB_PORT)

# Abre el archivo JSON y lee su contenido	
with open('./resources/Data_Mysql/locations.json', 'r') as archivo_json:	
    datos = json.load(archivo_json)	
    print(datos)


for i in range(0, len(datos), 1):	
    name=datos[i]['name']	
    city=datos[i]['city']	
    

    # por cada uno que lea, que haga un insert	
    location = Location(city, name) 	
    print(obj.insert_data2(location))	




