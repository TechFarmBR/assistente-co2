# ===========================
# Makefile - Assistente CO2
# ===========================

# Substitua se desejar outra porta
PORT=10000
IMAGE_NAME=assistente-co2

build:
	docker build -t $(IMAGE_NAME) .

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

restart:
	docker-compose restart

shell:
	docker exec -it assistente-co2-api /bin/bash

test:
	curl http://localhost:$(PORT)/ || true
