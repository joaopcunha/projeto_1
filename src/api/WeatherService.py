from commom import defines
import requests

class WeatherService:

    def __init__(self, api_key):
        self.__api_key = api_key

    def get_city_info(self, country_code, city):
        url = "{}/locations/v1/cities/{}/search?apikey={}&q={}".format(
            defines._API_URL_,
            country_code,
            self.__api_key,
            query
        )

        res = requests.get(
            url
        )

        return res.json()

    def get_city_conditions(self, city_code):
        url = "{}/currentconditions/v1/{}/historical/24?apikey={}".format(
            defines._API_URL_,
            city_code,
            self.__api_key
        )

        res = requests.get(
            url
        )

        return res.json()