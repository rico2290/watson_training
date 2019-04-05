import Modulo_mp3_to_wav as MMP3WAVE
import Modulo_Speech_to_Text as MST, json

name = "audio3.mp3"
output = "mp3_to_wav3.wav"

MMP3WAVE.convert_mp3_to_wav(name,output)

retorno_audio_to_text = MST.context_speech_to_text(output)
retorno_audio_to_text = retorno_audio_to_text.replace('"','')

print(json.dumps(retorno_audio_to_text,indent=2))

with open("retorno.txt","w", encoding="utf-8") as file:
    file.write(retorno_audio_to_text)
