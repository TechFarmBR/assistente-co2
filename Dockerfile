# Dockerfile para Assistente CO2
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe a porta da API
EXPOSE 10000

# Comando de inicialização
CMD ["uvicorn", "backend_assistente_co2:app", "--host", "0.0.0.0", "--port", "10000"]
