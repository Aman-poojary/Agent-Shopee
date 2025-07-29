# FastAPI Application

A simple FastAPI application with Docker support and Makefile for easy management.

## Features

- FastAPI application with health check endpoint
- Docker containerization
- Makefile for easy commands
- Development and production ready

## Quick Start

### Using Docker (Recommended)

1. **Build the Docker image:**
   ```bash
   make build
   ```

2. **Run the application:**
   ```bash
   make run
   ```

3. **Access the application:**
   - Health endpoint: http://localhost:8000/health
   - API documentation: http://localhost:8000/docs

### Development Mode

Run the application locally for development:
```bash
make dev
```

## Available Make Commands

- `make help` - Show all available commands
- `make build` - Build the Docker image
- `make run` - Run the application in Docker
- `make stop` - Stop the running container
- `make clean` - Remove Docker image and containers
- `make logs` - Show container logs
- `make dev` - Run locally for development

## API Endpoints

- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## Project Structure

```
.
├── app/
│   └── main.py          # FastAPI application
├── Dockerfile           # Docker configuration
├── Makefile            # Build and run commands
├── requirements.txt     # Python dependencies
├── .dockerignore       # Docker ignore file
└── README.md          # This file
``` 