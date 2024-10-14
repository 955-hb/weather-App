# import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('how is the weather where you are?')
        self.initUI()

    def initUI(self):
        self.inputLat()
        self.inputLon()
        self.quit_button = QPushButton('Close', self)
        self.quit_button.move(150, 300)
        self.quit_button.clicked.connect(self.close_program)

        # Label
        self.label = QtWidgets.QLabel(self)
        self.label.setText('gebe deine Position an.')
        self.label.move(150, 50)

        # Button
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(150, 250)
        self.btn1.setText('show me!')
        self.update()

    def inputLat(self):
        # Input Feld lat (Breitengrad) (QLineEdit)
        self.text_input = QtWidgets.QLineEdit(self)
        self.text_input.move(70, 100)
        self.text_input.resize(100, 20)

    def inputLon(self):
        # Input Feld lon (Längengrad)(QLineEdit)
        self.text_input = QtWidgets.QLineEdit(self)
        self.text_input.move(230, 100)
        self.text_input.resize(100, 20)

    def update(self):
        self.label.adjustSize()

        # Button close

    def close_program(self):
        print('das Programm wurde beendet!')
        QApplication.quit()


# eventuelle funktionen zur calculation!
'''       
    def on_click(self):
        # Eingabe holen
        user_input = self.text_input.text()
        # Übergibt den Input an eine Funktion
        self.handle_input(user_input)

    def handle_input(self, text):
        # Funktion, die den Input verarbeitet
        print(f"Eingabe erhalten: {text}")
        self.label.setText(f'Eingabe: {text}')  # Zeige die Eingabe im Label an
        self.label.adjustSize()  # Label Größe anpassen, damit Text hineinpasst
'''


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()


'''
API_Key = '2e26161e2980f3548c718d3630862b24'


# abfrage der Breiten- & Längen Angaben
lat = input('Gebe hier den Breitengrad ein: ')
lon = input('Gebe hier den Längengrad ein: ')


'''
# lat & len von Burg b. Magdeburg
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
'''
