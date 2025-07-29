from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, users, agent
from app.config import settings

# Create FastAPI app
app = FastAPI(
    title=settings.project_name,
    description="A FastAPI application with proper structure",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["health"])
app.include_router(users.router, prefix="/api/v1")
app.include_router(agent.router, prefix="/agent")

@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FastAPI Application",
        "docs": "/docs",
        "health": "/health"
    }