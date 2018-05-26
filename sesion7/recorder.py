import pyaudio
import wave

import speech_recognition as sr
class Recorder(object):
    
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    FILE_NAME = 'record.wav'
    audios = {'hola': 'hola.wav'}

    def __init__(self, file_name='record.wav', raspi=False):
        self.FILE_NAME = file_name
        self.audio = pyaudio.PyAudio()
        self.raspi = raspi
        self.r = sr.Recognizer()
    
    def talk(self, phrase):
        if self.raspi:
            phrase = "/home/pi/projects/robocholita/" + phrase
        wf = wave.open(phrase, 'rb')
        stream = self.audio.open(format=self.audio.get_format_from_width(wf.getsampwidth()),
                                    channels=wf.getnchannels(),
                                    rate=wf.getframerate(),
                                    output=True)
        data = wf.readframes(self.CHUNK)

        ## play
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(self.CHUNK)
        stream.stop_stream()
        stream.close()


    def listen(self, duration=3):
        # start recording
        if self.raspi == True:
            stream = self.audio.open(format=self.FORMAT,
                                    channels=1,
                                    rate=self.RATE,
                                    input_device_index = 2, 
                                    input=True,
                                    frames_per_buffer=self.CHUNK)
        else:
            stream = self.audio.open(format=self.FORMAT,
                                    channels=self.CHANNELS,
                                    rate=self.RATE,
                                    #input_device_index = input_index, 
                                    input=True,
                                    frames_per_buffer=self.CHUNK)
            
        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * duration)):
            data = stream.read(self.CHUNK, exception_on_overflow=False)
            frames.append(data)
            

                
        stream.stop_stream()
        stream.close()
        

        waveFile = wave.open(self.FILE_NAME, 'wb')
        if self.raspi:
            waveFile.setnchannels(1)
        else:
            waveFile.setnchannels(self.CHANNELS)
            
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

        with sr.AudioFile(self.FILE_NAME) as source:
            #print "->abriendo archivo..."
            audio = self.r.record(source)
        #print r.recognize_sphinx(audio)
        # print "->procesando"
        #print "--> convirtiendo audio..."
        self.raw_data = audio.get_raw_data(convert_rate=16000, convert_width=2)

    def getRaw(self):
        return self.raw_data

    def close(self):
        self.audio.terminate()

if __name__ == '__main__':
    r = Recorder()
    r.listen()
