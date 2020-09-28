import requests, json

base_url = "https://api.openweathermap.org/data/2.5/weather?"
city = input("Please write the city you want to know its weather: ")
api_key = "Write your API key"
url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
response = requests.get(url)

# checking the status code of the request
if response.status_code == 200:
   data = response.json()
   main = data['main']
   wind = data['wind']
   clouds = data['clouds']
   temp = main['temp']
   temp_min = main['temp_min']
   temp_max = main['temp_max']
   humidity = main['humidity']
   pressure = main['pressure']
   wind_speed = wind['speed']
   clouds_perc = clouds['all']
   report = data['weather']
   print(f"CITY: {city} \n")
   print(f"Temperature Now: {temp}")
   print(f"Temperature Min: {temp_min}")
   print(f"Temperature Max: {temp_max}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Wind speed: {wind_speed}")
   print(f"Cloud percentage: {clouds_perc}")
   print(f"Weather Report: {report[0]['description']}")
else:
   print("Something went wrong")
