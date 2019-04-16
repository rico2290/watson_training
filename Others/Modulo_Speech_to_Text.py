import speech_recognition as sr
import json

def context_speech_to_text(wav_audio_format):
        try:
                recognition = sr.Recognizer()
                escutar = sr.AudioFile(wav_audio_format)
                with escutar as source:
                        audio = recognition.record(source)
                        return json.dumps(recognition.recognize_google(audio))
        except:
                return print("Falha ao conectar com google") 


        

