#from pydub import AudioSegment
import subprocess, json


def convert_mp3_to_wav(file_to_convert, file_converted ):
    subprocess.call(['ffmpeg','-i',file_to_convert,file_converted])
    


