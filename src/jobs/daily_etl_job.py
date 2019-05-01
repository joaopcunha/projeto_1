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

def get_locations():

    locations = []

    for city in get_db_cities():
        api_city_info = api.get_city_info(
            "BR", "SP", city['city_name']
        )

        location_key = api_city_info[0]['Key']
        locations.append(
            {
                "city_id": city['id'],
                "city_name": city['city_name'],
                "location_key": location_key
            }
        )
    
    return locations

def run_job():

    locations = get_locations()

    for location in locations:
        api_city_conditions = api.get_city_conditions(location['location_key'])

        for condition in api_city_conditions:
            condition_date = condition['LocalObservationDateTime']
            precipitation = condition["PrecipitationSummary"]["PastHour"]["Metric"]["Value"]
            temperature = condition["Temperature"]["Metric"]["Value"]

            dbconn.insert(
                "INSERT INTO tbl_daily_city_conditions(observation_date, city_id, precipitation, temperature) VALUES (%s, %s, %s, %s)",
                [condition_date, city['city_id'], precipitation, temperature]
            )

if __name__ == '__main__':
    run_job()
