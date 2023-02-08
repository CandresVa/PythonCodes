import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

#Voices in my machine:
id1='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

#Use our mic and give bact the text
def Transform_audio_to_text():
    #Save the recogizer in variable
    r = sr.Recognizer()
    #Config the mic
    with sr.Microphone() as origen:
        #Time to wait
        r.paure_threshold = 0.8

        #Infor the start of the recor:
        print('Now you can speak')

        #Save the heard it
        audio = r.listen(origen)

        #
        try:
            #Look in google
            request = r.recognize_google(audio, language="es-ool")
            #Test
            print('You said: '+request)
            #Return
            return request
        #If it is not understand
        except sr.UnknownValueError:
            #Test
            print('Ups, no understand')
            #Give back error
            return 'Kepp waiting'
        #
        except sr.RequestError:
            # Test
            print('Ups, no service')
            # Give back error
            return 'Kepp waiting'
        #Unspected error:
        except:
            # Test
            print('Ups, something wrong')
            # Give back error
            return 'Kepp waiting'

Transform_audio_to_text()

#Funtion, the assiance can be hear

def talk(message):
    #start the pyttsx3
    engine =pyttsx3.init()
    engine.setProperty('voice', id2)

    #Talk the message
    engine.say(message)
    engine.runAndWait()

def hablar(mensaje):
    # start the pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # Talk the message
    engine.say(mensaje)
    engine.runAndWait()


talk('Hello world, I´m here to cause controversy')
hablar('Hola mundo, estoy aquí para causar controversia')

engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
#Voice options
def request_day():
    #Create day variables
    day=datetime.date.today()
    print(day)

    #Create variable for day week
    day_week = day.weekday()
    print(day_week)

    #Dictionary
    calendar = {0:'Lunes',
                1:'Martes',
                2:'Miercoles',
                3:'Jueves',
                4:'Viernes',
                5:'Sábado',
                6:'Domingo'}
    talk(f'Today is {calendar[day_week]}')
    hablar(f'Hoy es {calendar[day_week]}')
request_day()

#Inform the hour
def request_hour():
    hour = datetime.datetime.now()
    print(hour)
    talk(hour)
    hablar(hour)


    #More datailed
    hour = f'In this moment is {hour.hour} hours {hour.minute} minutes and {hour.minute} seconds.'
    talk(hour)
request_hour()


#First wave
def initial_wave():
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        moment = 'Good night'
    elif 6 <= hour.hour < 13:
        moment = 'Good morning'
    else:
        moment = 'Good afternoon'
    talk(f'{moment}, soy Zula, your virtual assistance. Please, toll me haw can I help you?')

initial_wave()

# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    initial_wave()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = Transform_audio_to_text().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            request_day()
            continue
        elif 'qué hora es' in pedido:
            request_hour()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break
pedir_cosas()