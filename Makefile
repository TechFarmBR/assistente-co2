# ===========================
# Makefile - Assistente CO2
# ===========================

PORT=10000
IMAGE_NAME=assistente-co2
CONTAINER_NAME=assistente-co2-api

# Build da imagem Docker
build:
	docker build -t $(IMAGE_NAME) .

# Subir containers com Docker Compose
up:
	docker-compose up -d

# Derrubar os containers
down:
	docker-compose down

# Logs do container
logs:
	docker-compose logs -f

# Reiniciar containers
restart:
	docker-compose restart

# Acessar terminal do container
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Testar se a API está online localmente
test:
	curl http://localhost:$(PORT)/ || true

# Executar localmente sem Docker (modo dev)
run:
	uvicorn backend_assistente_co2:app --reload --host 0.0.0.0 --port $(PORT)

# Instalar dependências no ambiente local
install:
	pip install -r requirements.txt

# Atualizar pip
upgrade-pip:
	python -m pip install --upgrade pip
