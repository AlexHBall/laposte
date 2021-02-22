from app import request_handler

def get_many_details():
    cities = ['London','Bordeaux']
    for city in cities:
        print(request_handler.get_weather_city_name(city))