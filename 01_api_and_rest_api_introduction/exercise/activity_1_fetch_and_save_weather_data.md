# Exercises on Rest API response parsing and storage

## Fetch and Save Weather Data

### Objective:
Practice making a GET request to a public API, parsing the JSON response, and saving specific information to a CSV file.

### Scenario:
You want to keep a record of the current weather in your city. Use the [Open-Meteo](https://open-meteo.com/) API (no authentication required) to fetch the temperature and weather condition for a city, then save the results as a CSV file.

### Instructions:

1. Write a Python script that:

   - Sends a GET request to retrieve the current weather for a city of your choice.
   - Parses the temperature and weather description from the response JSON.
   - Map weather_code to a description. Use below table for mapping.
   - Appends this data (date, time, temperature, condition) to a CSV file called weather_log.csv.

2. Run the script and check that your CSV contains the latest weather.

##### Open-Meteo Weather Codes

| Code | Description              |
|------|--------------------------|
| 0    | Clear sky                |
| 1    | Mainly clear             |
| 2    | Partly cloudy            |
| 3    | Overcast                 |
| 45   | Fog                      |
| 48   | Depositing rime fog      |
| 51   | Light drizzle            |
| 53   | Drizzle                  |
| 55   | Dense drizzle            |
| 61   | Slight rain              |
| 63   | Rain                     |
| 65   | Heavy rain               |
| 80   | Rain showers             |
| 95   | Thunderstorm             |

