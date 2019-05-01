#TODO
#Fazer script que cria as tabelas do warehouse

#tbl_cities
#Id da cidade (chave primaria), nome da cidade (determinados), altitude, número de habitantes

#tbl_daily_city_conditions
#timestamp, id da cidade, precipitação, temp minima, temp máxima, amplitude termica
#timestamp + id da cidade são chave unica em conjunto
import sys

sys.path.append("./commom")
sys.path.append("./dbconn")

from DbConnectionPSQL import DbConnectionPSQL
import defines

dbconn = DbConnectionPSQL(
    defines._PSQL_HOST_,
    defines._PSQL_USER_,
    defines._PSQL_PASSWORD_,
    defines._PSQL_DB_
)

create_city_table_query = '''
CREATE TABLE IF NOT EXISTS tbl_cities
(id INT PRIMARY KEY NOT NULL,
city_name VARCHAR NOT NULL,
elevation INT,
population INT,
location_key INT
)
'''

create_daily_city_conditions_query = '''
CREATE TABLE IF NOT EXISTS tbl_daily_city_conditions
(observation_date TIMESTAMP,
city_id INT,
daily_temperature_amplitude INT,
UNIQUE (observation_date, city_id)
)
'''


create_hour_city_conditions_query = '''
CREATE TABLE IF NOT EXISTS tbl_hour_city_conditions
(observation_date TIMESTAMP,
city_id INT,
precipitation INT,
temperature INT,
UNIQUE (observation_date, city_id)
)
'''

insert_query = "INSERT INTO tbl_cities(id, city_name) VALUES (%s, %s)"
list_of_values = [
    [1, "São Paulo"],
    [2, "Santos"]
    # [3, "Ribeirão Preto"],
    # [4, "Sorocaba"],
    # [5, "São José dos Campos"],
    # [6, "Atibaia"],
    # [7, "Bauru"],
    # [8, "Presidente Prudente"],
    # [9, "Campinas"],
    # [10, "Campos do Jordão"]
]

dbconn.run_query(create_city_table_query)

for values in list_of_values:
    dbconn.insert(insert_query, values)

dbconn.run_query(create_hour_city_conditions_query)
dbconn.run_query(create_daily_city_conditions_query)
dbconn.close_connection()