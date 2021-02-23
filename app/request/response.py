from datetime import datetime
from json import dumps

class Response():
    def __init__(self,response_json):
        self.json = response_json
        self.name = response_json['name']
        self.weather_string = response_json['weather'][0]['main']
        tmp = response_json['main']
        self.temp_feels_like = tmp['feels_like']
        self.temp_min = tmp['temp_min']
        self.temp_max = tmp['temp_max']
        sys = response_json['sys']
        self.country = sys['country']
        self.sunrise = sys['sunrise']
        self.sunset = sys['sunset']

    def get_json(self):
        return dumps({
            'name' : self.name,
            'current_weather' : self.weather_string,
            'temp_max' : self.temperature_to_celcius(self.temp_max),
            'temp_min' : self.temperature_to_celcius(self.temp_min),
            'feels_like' : self.temperature_to_celcius(self.temp_feels_like),
            'sunrise' : self.get_sunrise_24h(),
            'sunset' : self.get_sunset_24h(),
        })


    def get_sunrise_24h(self):
        dt = datetime.fromtimestamp(self.sunrise)
        return dt.strftime("%H:%M")

    def get_sunset_24h(self):
        dt = datetime.fromtimestamp(self.sunset)
        return dt.strftime("%H:%M")

    def temperature_to_celcius(self,temp):
        return round(temp - 273.15,2)