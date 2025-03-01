# 🎙️ Transcrição de Áudio com Whisper

Este projeto utiliza o modelo **Whisper**, desenvolvido pela OpenAI, para realizar a transcrição automática de arquivos de áudio. O código foi baseado no repositório oficial: [Whisper - OpenAI](https://github.com/openai/whisper).

## 📋 Requisitos
Antes de executar o código, certifique-se de que os seguintes requisitos estão instalados no seu sistema:

1. **Python** (3.7 ou superior) → [Download Python](https://www.python.org/downloads/)
2. **FFmpeg** → [Guia de instalação do FFmpeg](https://ffmpeg.org/download.html)
3. **Whisper** (Biblioteca OpenAI Whisper)
4. **python-dotenv** (Para carregar variáveis de ambiente)

Para instalar as dependências, execute os seguintes comandos:
```sh
pip install -U openai-whisper
pip install ffmpeg-python
pip install python-dotenv
```

---
## 🚀 Como Usar
1. Clone ou baixe este repositório.
2. No arquivo `.env` modifique as variáveis:

```
CAMINHO_ARQUIVO="C:/caminho/para/seu/arquivo.mp3"
CAMINHO_TRANSCRICAO="C:/caminho/para/salvar/transcricao.txt"
MODELO="large"
```
> **Observação:** O caminho do arquivo deve estar entre **aspas duplas** (`""`), utilizar **barras normais (`/`)** e conter um **nome de arquivo de saída com extensão `.txt`**.

3. Execute o script Python:
```sh
python transcrever.py
```

Após a execução, a transcrição será salva no arquivo especificado em `CAMINHO_TRANSCRICAO`.

---
## 📌 Modelos Disponíveis no Whisper
O Whisper possui diferentes modelos de transcrição, que variam em velocidade e precisão. Escolha o modelo mais adequado para sua necessidade:

| Modelo  | Velocidade de reprodução do áudio  | Precisão   | Consumo de Processamento|
|---------|------------------------------------|------------|-------------------------|
| `tiny`  | Muito rápido (10x)                 | Menor      | Baixo                   |
| `base`  | Rápido (7x)                        | Boa        | Moderado                |
| `small` | Médio (4x)                         | Melhor     | Considerável            |
| `medium`| Lento (2x)                         | Muito Boa  | Alto                    |
| `large` | Mais lento (1x)                    | Máxima     | Muito Alto              |

> **Observação:** O tempo de execução é o tempo do áudio dividido pela velocidade de reprodução mais o tempo de processamento, que podem variar dependendo do desempenho do computador.

Para utilizar um modelo específico, basta definir a variável `MODELO` no arquivo `.env`, por exemplo:

```
MODELO="medium"
```

---
## 📚 Referências
- [Repositório Oficial Whisper - OpenAI](https://github.com/openai/whisper)
