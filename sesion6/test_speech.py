import datetime
import speech_recognition as sr

r = sr.Recognizer()
comandos = ["saluda", "despedida", "hora", "fecha"]
respuestas = {"saluda": "hola! que tal!",
                "despedida": "hasta luego!",
                "hora": "son las " + str(datetime.datetime.now().hour),
                "fecha": "hoy es " + str(datetime.datetime.now())}
run = True
while run:
    print("presiona para hablar...")
    a = raw_input()

    with sr.Microphone() as source:
        print("di algo: ")
        audio = r.listen(source)

    texto = r.recognize_sphinx(audio, language="es-ES")
    for comando in comandos:
        if comando in texto:
            print(respuestas[comando])
            if comando == "despedida":
                run = False

    

