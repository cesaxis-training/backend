# Quotes API Backend

A RESTful API service for managing quotes, built with Python/Flask, containerized with Docker and automated with CI/CD workflows.

## Overview

This backend service provides API endpoints to manage a collection of quotes, supporting full CRUD (Create, Read, Update, Delete) operations.

## Features

- RESTful API endpoints with Flask
- CRUD operations for quotes
- Docker containerization
- CI/CD pipelines with GitHub Actions

## Project Structure

```
backend/
├── src/
│   ├── controllers/
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   └── app.py
├── .github/
│   └── workflows/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## API Endpoints

| Method | Endpoint        | Description               |
| ------ | --------------- | ------------------------- |
| GET    | /api/quotes     | Retrieve all quotes       |
| GET    | /api/quotes/:id | Retrieve a specific quote |
| POST   | /api/quotes     | Create a new quote        |
| PUT    | /api/quotes/:id | Update an existing quote  |
| DELETE | /api/quotes/:id | Delete a quote            |

## Getting Started

1. Clone the repository:

```bash
git clone git@github.com:cesaxis-training/backend.git
cd backend
```

2. Run with Docker:

```bash
docker-compose up --build
```
## To use database

```bash
docker compose exec db mysql -p 

//password="password do root"

```

```sql
    show database;

    use mydatabase;

    CREATE TABLE quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(500) NOT NULL,
    author VARCHAR(100) NOT NULL
);