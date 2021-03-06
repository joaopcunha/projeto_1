import sys

sys.path.append("./commom")
sys.path.append("./dbconn")
sys.path.append("./api")

from DbConnectionPSQL import DbConnectionPSQL
from WeatherService import WeatherService
import defines

dbconn = DbConnectionPSQL(
    defines._PSQL_HOST_,
    defines._PSQL_USER_,
    defines._PSQL_PASSWORD_,
    defines._PSQL_DB_
)

api = WeatherService(
    defines._API_KEY_
)

def get_db_cities():
    return dbconn.select("SELECT * FROM tbl_cities")

def run_job():
    print("Running city info job...")
    db_cities = get_db_cities()

    for city in db_cities:
        city_name = city['city_name']
        api_city_info = api.get_city_info(
            "BR", "SP", city_name
        )

        city_population = api_city_info[0]['Details']['Population']
        city_elevation = api_city_info[0]['GeoPosition']['Elevation']['Metric']["Value"]
        location_key = api_city_info[0]['Key']

        dbconn.run_query(
            "UPDATE tbl_cities SET population = {}, elevation = {}, location_key = {} WHERE city_name = '{}'".format(
                city_population, 
                city_elevation,
                location_key,
                city_name
            )
        )
    
    print("City info job successfull")
    dbconn.close_connection()

if __name__ == '__main__':
    run_job()

