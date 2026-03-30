import requests
import json
import csv

#Meteo endpoint
url = 'https://api.open-meteo.com/v1/forecast'

# Make the GET request
response = requests.get(url,params=	{"latitude": 52.5244,"longitude": 13.4105,"hourly": "temperature_2m","models": "icon_seamless","current": ["temperature_2m", "weather_code"],"timezone": "Europe/Berlin","forecast_days": 1})

parsed_weather = response.json()
# print(json.dumps(parsed_weather, indent=2)
      
# Export to csv, (date, time, temperature, condition)

#check that variable can be splitted
#print(parsed_weather['current']['time'])
#print(parsed_weather['current']['temperature_2m'])
#print(parsed_weather['current']['weather_code'])


time = parsed_weather['current']['time']
temperature = parsed_weather['current']['temperature_2m']
weather_code = parsed_weather['current']['weather_code']


#create weather code dictionary
weather_codes = {0:'Clear sky',1:'Mainly clear',2:'Partly cloudy',3:'Overcast',45:'Fog',48:'Depositing rime fog',51:'Light drizzle',53:'Drizzle',55:'Dense drizzle',61:'Slight rain',63:'Rain',65:'Heavy rain',80:'Rain showers',95:'Thunderstorm'}
#print(weather_codes[weather_code])
condition = weather_codes[weather_code]

#fix time variable to be as date and time
splitted_time = time.split("T")
date = splitted_time[0]
time = splitted_time [1]
#print(date)
#print(time)


with open("weather_log.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([date, time, temperature, condition])