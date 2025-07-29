# Project Structure for Shopping Assistant AI Agent

## Backend (FastAPI + LangChain + FAISS)

app/
├── main.py                  # FastAPI entrypoint
├── config.py                # Configuration settings
├── database/                # DB connection logic
├── models/
│   ├── user.py              # User models
│   └── product.py           # Product models
├── routes/
│   ├── users.py             # User endpoints
│   ├── health.py            # Health check
│   └── products.py          # Product search endpoints
├── services/
│   ├── user_service.py      # User logic
│   └── product_service.py   # Product search logic, FAISS integration
├── utils/
│   ├── helpers.py           # General helpers
│   └── faiss_utils.py       # FAISS indexing/search helpers
├── tests/
│   ├── test_health.py       # Health check tests
│   └── test_products.py     # Product search tests
└── data/
    ├── products.csv         # Product catalog
    └── faiss_index/         # FAISS index files

## Frontend (Streamlit)

frontend/
├── streamlit_app.py         # Streamlit app for user interaction
├── STREAMLIT_INTEGRATION.md # Streamlit integration guide

## Shared/Root

- requirements.txt           # Python dependencies
- docker-compose.yml         # Docker orchestration
- Dockerfile                 # Backend Dockerfile
- Dockerfile.streamlit       # Streamlit Dockerfile
- .gitignore
- README.md

---

This structure supports a modular backend (FastAPI, LangChain, FAISS) and a Streamlit frontend for the AI shopping assistant experience. 