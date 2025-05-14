# FastAPI Clean Architecture

This project is a FastAPI application that implements a clean code architecture

## Project Structure

```
fastapi-clean-architecture
├── app
│   ├── api
│   │   ├── endpoints
│   │   │   └── upload_csv.py
│   │   └── __init__.py
│   ├── core
│   │   ├── config.py
│   │   └── __init__.py
│   ├── db
│   │   ├── base.py
│   │   ├── session.py
│   │   └── __init__.py
│   ├── models
│   │   ├── csv_data.py
│   │   └── __init__.py
│   ├── schemas
│   │   ├── csv_data.py
│   │   └── __init__.py
│   ├── services
│   │   ├── csv_service.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
├── migrations
│   └── README.md
├── tests
│   ├── test_upload_csv.py
│   └── __init__.py
├── .env
├── requirements.txt
└── README.md
```