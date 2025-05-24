# Dockerfile para Assistente CO2 com suporte a OCR e FastAPI

FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    python3-dev \
    tesseract-ocr \
    tesseract-ocr-por \
    poppler-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para dentro do contêiner
COPY . .

# Instala as dependências Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta
EXPOSE 10000

# Comando de inicialização
CMD ["uvicorn", "backend_assistente_co2:app", "--host", "0.0.0.0", "--port", "10000"]
