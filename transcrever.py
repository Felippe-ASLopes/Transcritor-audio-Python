import whisper
import os
from dotenv import load_dotenv

load_dotenv()

caminhoArquivo = os.getenv("CAMINHO_ARQUIVO")
caminhoTranscricao = os.getenv("CAMINHO_TRANSCRICAO")
modelo = os.getenv("MODELO")

if not caminhoArquivo or not caminhoTranscricao:
    raise ValueError("As variáveis de ambiente CAMINHO_ARQUIVO_AUDIO ou CAMINHO_TRANSCRICAO não estão definidas!")

api = whisper.load_model(modelo)

resposta = api.transcribe(caminhoArquivo)

print("Transcrição:")
print(resposta["text"])

with open(caminhoTranscricao, "w", encoding="utf-8") as arquivo:
    arquivo.write(resposta["text"])

print("Transcrição concluída!")