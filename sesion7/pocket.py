import os
from os import path
from pocketsphinx import pocketsphinx
from pocketsphinx import Decoder

from recorder import Recorder

import speech_recognition as sr

import serial

arduino = serial.Serial("/dev/ttyACM0", 9600)
# carpeta con el modelo
MODELDIR = "es-ES"
ac_model = "acoustic-model"

pr_dic = "pronounciation-dictionary.dict"

grammar = "gram/comandos.gram"

config = Decoder.default_config()
config.set_string('-hmm', "es-ES/acoustic-model")
config.set_string('-dict', "es-ES/pronounciation-dictionary.dict")
config.set_string('-jsgf', "gram/comandos.gram")
config.set_string('-logfn', os.devnull)


# objeto decoder de pocketsphinx
decoder = Decoder(config)
r = sr.Recognizer()

# herramienta para grabar audio
recorder = Recorder()

# escucha un tiempo y luego reconoce
print("di algo")
recorder.listen(2)
raw_data = recorder.getRaw()
print("reconociendo...")
####
import serial
arduino = serial.Serial("/dev/ttyACM0", 9600)

try:
        decoder.start_utt()
        decoder.process_raw(raw_data, False, True)
        decoder.end_utt()
        hyp = decoder.hyp()
        print("dijiste: ", hyp.hypstr)
        com_array = hyp.hypstr.split()
        print(com_array)

        if(com_array[0] == "encender"):
                arduino.write('e')
        elif(com_array[0] == "apagar"):
                arduino.write('a')
except Exception:
        print(Exception.message)