import requests

API_Key = '2e26161e2980f3548c718d3630862b24'


# abfrage der Breiten- & Längen Angaben
lat = input('Gebe hier den Breitengrad ein: ')
lon = input('Gebe hier den Längengrad ein: ')


'''
#lat & len von Burg b. Magdeburg
# latitude (Breitengrad)
lat = '52.270901'

# longitude (Längengrad)
lon = '11.855350'
'''


# API
request_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    
    weather_description = data['weather'][0]['description']
    city = data['name']
    temperature = round(data['main']['temp']-273.15) #Kelvin --> Celsius
    feelsLike = round(data['main']['feels_like']-273.15)
    
    
    # ausgabe Wetter-Informationen
    print(f'In {city} herscht grad folgendes Wetter : ')
    
    # Temperatur
    print(str(temperature) + ' °celsius')
    
    # Bewölkt?
    print(weather_description)
    
    # gefühlt wie
    print('Gefühlt wie: ' + str(feelsLike) + ' °celsius')
    
    
else:
    print('Fehler bei der Abfrage! ')
