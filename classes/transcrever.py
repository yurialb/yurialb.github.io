#transcritor de audio

import whisper

# Modelos tiny (rapido); base; small; medium; large (muito lento).
modelo = whisper.load_model("large")

file = open("transcricao.txt","w")

#transcricao = modelo.transcribe("nome_do_arquivo_de_audio.mp3")
transcricao = modelo.transcribe("Gravando.m4a")

file.write(transcricao)
file.close()
