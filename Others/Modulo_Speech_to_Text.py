import speech_recognition as sr
import json

def context_speech_to_text(wav_audio_format):
    #recognition.recognize_google(output,language="pt-br")
    recognition = sr.Recognizer()
    escutar = sr.AudioFile(wav_audio_format)
    with escutar as source:
        audio = recognition.record(source)
        return json.dumps(recognition.recognize_google(audio)) 

