.PHONY: build run stop clean logs help dev streamlit docker-compose-up docker-compose-down

# Default target
help:
	@echo "Available commands:"
	@echo "  build    - Build the Docker image"
	@echo "  run      - Run the FastAPI application in Docker"
	@echo "  stop     - Stop the running container"
	@echo "  clean    - Remove Docker image and containers"
	@echo "  logs     - Show container logs"
	@echo "  dev      - Run the FastAPI application locally for development"
	@echo "  streamlit - Run Streamlit UI locally"
	@echo "  docker-compose-up - Run both FastAPI and Streamlit with Docker Compose"
	@echo "  docker-compose-down - Stop Docker Compose services"

# Build the Docker image
build:
	docker build -t fastapi-app .

# Run the application in Docker
run:
	docker run -d --name fastapi-container -p 8000:8000 fastapi-app

# Stop the running container
stop:
	docker stop fastapi-container || true
	docker rm fastapi-container || true

# Clean up Docker resources
clean: stop
	docker rmi fastapi-app || true

# Show container logs
logs:
	docker logs -f fastapi-container

# Run locally for development
dev:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run Streamlit UI locally
streamlit:
	streamlit run streamlit_app.py --server.port 8501

# Run both services with Docker Compose
docker-compose-up:
	docker-compose up -d

# Stop Docker Compose services
docker-compose-down:
	docker-compose down 