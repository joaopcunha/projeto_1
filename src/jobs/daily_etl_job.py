import sys
from datetime import datetime

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
        locations.append(
            {
                "city_id": city['id'],
                "location_key": city['location_key']
            }
        )
    
    return locations

def populate_hour_condition(location, api_city_conditions):
    for condition in api_city_conditions:
        condition_date = condition['LocalObservationDateTime']
        precipitation = condition["PrecipitationSummary"]["PastHour"]["Metric"]["Value"]
        temperature = condition["Temperature"]["Metric"]["Value"]

        dbconn.insert(
            "INSERT INTO tbl_hour_city_conditions(observation_date, city_id, precipitation, temperature) VALUES (%s, %s, %s, %s)",
            [condition_date, location['city_id'], precipitation, temperature]
        )

def populate_daily_condition(location, api_city_conditions):
    for condition in api_city_conditions:
        condition_date = condition['LocalObservationDateTime']

        if condition_date[11:13] == "23":
            min_day_temperature = condition['TemperatureSummary']['Past24HourRange']['Minimum']['Metric']['Value']
            max_day_temperature = condition['TemperatureSummary']['Past24HourRange']['Maximum']['Metric']['Value']
            daily_temperature_amplitude = max_day_temperature - min_day_temperature

            dbconn.insert(
                "INSERT INTO tbl_daily_city_conditions(observation_date, city_id, daily_temperature_amplitude) VALUES (%s, %s, %s)",
                [condition_date, location['city_id'], daily_temperature_amplitude]
            )

def run_job():
    print("Running daily jobs...")

    locations = get_locations()

    for location in locations:
        api_city_conditions = api.get_city_conditions(location['location_key'])
        populate_hour_condition(location, api_city_conditions)
        populate_daily_condition(location, api_city_conditions)
        
    print("Daily jobs successfull")

if __name__ == '__main__':
    run_job()
