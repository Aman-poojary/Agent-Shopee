# FastAPI Project Structure Guide

## 📁 Complete Project Structure

```
fastapi-app/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py               # Application configuration
│   │
│   ├── routes/                 # API Route handlers
│   │   ├── __init__.py
│   │   ├── health.py          # Health check endpoints
│   │   └── users.py           # User-related endpoints
│   │
│   ├── models/                 # Pydantic data models
│   │   ├── __init__.py
│   │   └── user.py            # User data models
│   │
│   ├── services/               # Business logic layer
│   │   ├── __init__.py
│   │   └── user_service.py    # User business logic
│   │
│   ├── database/               # Database configuration
│   │   ├── __init__.py
│   │   └── connection.py      # Database connection setup
│   │
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py         # Common helper functions
│   │
│   └── tests/                  # Test files
│       ├── __init__.py
│       └── test_health.py     # Health endpoint tests
│
├── requirements.txt            # Python dependencies
├── Dockerfile                 # Docker configuration
├── Makefile                   # Build and run commands
├── .dockerignore             # Docker ignore file
├── README.md                 # Project documentation
└── PROJECT_STRUCTURE.md      # This file
```

## 🗂️ Folder Explanations

### 📂 `app/routes/` - API Route Handlers
**Purpose**: Contains all API endpoint definitions using FastAPI routers.

**What goes here**:
- Route handlers for different API endpoints
- Request/response validation
- URL parameter handling
- HTTP method definitions (GET, POST, PUT, DELETE)

**Example structure**:
```
routes/
├── health.py      # Health check endpoints
├── users.py       # User management endpoints
├── auth.py        # Authentication endpoints
├── products.py    # Product-related endpoints
└── orders.py      # Order management endpoints
```

**Key concepts**:
- Use `APIRouter()` for modular routing
- Group related endpoints together
- Use tags for API documentation organization
- Keep routes thin - delegate business logic to services

### 📂 `app/models/` - Data Models
**Purpose**: Pydantic models for data validation and serialization.

**What goes here**:
- Request/response models
- Database models (if using SQLAlchemy)
- Data validation schemas
- API documentation models

**Example structure**:
```
models/
├── user.py        # User-related models
├── product.py     # Product models
├── order.py       # Order models
└── common.py      # Shared/base models
```

**Key concepts**:
- Use Pydantic for automatic validation
- Separate input/output models
- Use inheritance for shared fields
- Include proper type hints

### 📂 `app/services/` - Business Logic Layer
**Purpose**: Contains all business logic and data processing.

**What goes here**:
- Business rules and logic
- Data processing functions
- External API integrations
- Complex calculations

**Example structure**:
```
services/
├── user_service.py     # User business logic
├── auth_service.py     # Authentication logic
├── email_service.py    # Email sending logic
├── payment_service.py  # Payment processing
└── notification_service.py  # Notification logic
```

**Key concepts**:
- Keep business logic separate from routes
- Make services reusable
- Handle complex operations
- Include proper error handling

### 📂 `app/database/` - Database Configuration
**Purpose**: Database connection and configuration management.

**What goes here**:
- Database connection setup
- Session management
- Migration files
- Database utilities

**Example structure**:
```
database/
├── connection.py   # Database connection
├── models.py       # SQLAlchemy models
├── migrations/     # Database migrations
└── repositories/   # Data access layer
```

### 📂 `app/utils/` - Utility Functions
**Purpose**: Common helper functions and utilities.

**What goes here**:
- Helper functions
- Common utilities
- Shared constants
- Helper classes

**Example structure**:
```
utils/
├── helpers.py      # General helper functions
├── validators.py   # Custom validation functions
├── constants.py    # Application constants
└── decorators.py   # Custom decorators
```

### 📂 `app/tests/` - Test Files
**Purpose**: Unit tests, integration tests, and test utilities.

**What goes here**:
- Unit tests for each module
- Integration tests
- Test fixtures and utilities
- Mock data

**Example structure**:
```
tests/
├── test_routes/    # Route tests
├── test_services/  # Service tests
├── test_models/    # Model tests
├── conftest.py     # Test configuration
└── factories.py    # Test data factories
```

## 🔄 Data Flow

```
Client Request
    ↓
Routes (app/routes/)
    ↓
Models (app/models/) - Validation
    ↓
Services (app/services/) - Business Logic
    ↓
Database (app/database/) - Data Access
    ↓
Response (Models) - Serialization
    ↓
Client Response
```

## 🎯 Best Practices

### Routes (`app/routes/`)
- Keep routes thin - delegate to services
- Use proper HTTP status codes
- Include comprehensive error handling
- Use dependency injection for database sessions
- Group related endpoints with prefixes

### Services (`app/services/`)
- Contain all business logic
- Be stateless when possible
- Handle complex operations
- Include proper error handling
- Make services testable

### Models (`app/models/`)
- Use Pydantic for validation
- Separate input/output models
- Include proper documentation
- Use inheritance for shared fields
- Include example data for API docs

### Database (`app/database/`)
- Use SQLAlchemy for ORM
- Implement proper session management
- Use migrations for schema changes
- Include connection pooling
- Handle database errors gracefully

## 🚀 Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   make dev
   ```

3. **Access the API**:
   - Health check: http://localhost:8000/health
   - API docs: http://localhost:8000/docs
   - Users API: http://localhost:8000/api/v1/users

4. **Run tests**:
   ```bash
   pytest app/tests/
   ```

This structure provides a scalable, maintainable, and testable FastAPI application with clear separation of concerns. 