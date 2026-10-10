# 💰 PennyTrack

> A simple RESTful API for organizing and monitoring your personal finances.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

PennyTrack helps keep personal financial activity in one place through a fast, structured, and easy-to-use API.

## ✨ Features

- 📈 Track income
- 📉 Record expenses
- 🔄 Manage financial transactions

## 🛠️ Tech Stack

| Technology | Purpose |
| --- | --- |
| **Python** | Application development |
| **FastAPI** | RESTful API framework |
| **PostgreSQL** | Data storage |

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL

### Installation

```bash
git clone <repository-url>
cd finance-app
uv sync
```

Create a PostgreSQL database named `penny_track`, then configure the connection string
through the `DATABASE_URL` environment variable:

```powershell
$env:DATABASE_URL = "postgresql+psycopg://postgres:your_password@localhost:5432/penny_track"
uv run uvicorn penny_track.main:app --reload
```

The URL uses the `psycopg` driver already declared in `pyproject.toml`. For local
development, copy `.env.example` to `.env` and replace the placeholder values;
load those variables in your terminal or through your VS Code launch configuration.

## 📖 API Documentation

When the application is running, FastAPI provides interactive documentation at:

- `/docs` — Swagger UI
- `/redoc` — ReDoc

## 📌 Overview

PennyTrack provides a focused foundation for managing income, expenses, and financial transactions through a RESTful interface.

## 📄 License

License information has not been defined yet.
