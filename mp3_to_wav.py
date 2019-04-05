from pydub import AudioSegment
import subprocess

name = "C:/Users/102869/Desktop/watson_training/Others/audio.mp3"
output = "C:/Users/102869/Desktop/watson_training/Others/mp3_to_wav.wav"

subprocess.call(['ffmpeg','-i', name,output])


