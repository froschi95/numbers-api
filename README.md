# Numbers API

## Description
Numbers API is a FastAPI-based application that provides various number classifications and fun facts about numbers.

## Features
- Classify numbers as prime, perfect, Armstrong, odd, or even.
- Calculate the sum of the digits of a number.
- Fetch fun facts about numbers from an external API.

## Requirements
- Python 3.12 or higher
- FastAPI
- HTTPX

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/froschi95/numbers-api.git
cd numbers-api
```

2. Create and activate a virtual environment using uv:
```bash
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install the project with development dependencies:
```bash
uv pip install -e ".[dev]"
```

4. Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## 🔍 API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## 🧪 Running Tests

```bash
pytest
```

## 📁 Project Structure

```
.
├── app
│   ├── exceptions
│   │   ├── handler.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── handler.cpython-313.pyc
│   │       └── __init__.cpython-313.pyc
│   ├── __init__.py
│   ├── main.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   └── main.cpython-313.pyc
│   ├── routes
│   │   ├── __init__.py
│   │   ├── number.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-313.pyc
│   │       └── number.cpython-313.pyc
│   └── services
│       ├── classification.py
│       ├── fun_fact.py
│       ├── __init__.py
│       └── __pycache__
│           ├── classification.cpython-313.pyc
│           ├── fun_fact.cpython-313.pyc
│           └── __init__.cpython-313.pyc
├── pyproject.toml
├── README.md
└── uv.lock
```

## 🛠️ Development

The project uses `pyproject.toml` for dependency management and build configuration. Dependencies are divided into these groups:

- `dependencies`: Core project dependencies
- `dev-dependencies`: Development tools (testing, linting, etc.)
