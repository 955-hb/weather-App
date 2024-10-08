import requests

API_Key = '2e26161e2980f3548c718d3630862b24'


#lat & len von Burg b. Magdeburg
# latitude (Breitengrad)
lat = '52.270901'

# longitude (Längengrad)
lon = '11.855350'

request_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather_description = data['weather'][0]['description']
    #print(weather_description)
    city = data['name']
    print(city)
    temperature = round(data['main']['temp']-273.15) #Kelvin --> Celsius
    print(str(temperature) + ' °celsius')
else:
    print('Fehler bei der Abfrage! ')
