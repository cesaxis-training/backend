# Quotes API Backend

A RESTful API service for managing quotes, built with Python/Flask, containerized with Docker, and automated with CI/CD workflows.

## Overview

This backend service provides API endpoints to manage a collection of quotes, supporting full CRUD (Create, Read, Update, Delete) operations.

## Features

- RESTful API endpoints with Flask
- CRUD operations for quotes
- Docker containerization
- CI/CD pipelines with GitHub Actions

## API Endpoints

| Method | Endpoint        | Description               |
| ------ | --------------- | ------------------------- |
| GET    | /api/quotes     | Retrieve all quotes       |
| GET    | /api/quotes/:id | Retrieve a specific quote |
| POST   | /api/quotes     | Create a new quote        |
| PUT    | /api/quotes/:id | Update an existing quote  |
| DELETE | /api/quotes/:id | Delete a quote            |

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone git@github.com:cesaxis-training/backend.git
   cd backend
   ```

2. **Setup environment variables:**

   ```bash
   cp .env.example .env
   ```

3. **Run with Docker:**

   ```bash
   docker-compose up --build
   ```

## Database Usage

To interact with the database, use the following command:

```bash
docker compose exec db mysql -p
```

The schema is defined in the `models.py` file and automatically created when the container starts if it doesn't exist.

## Disclaimer

This project is for educational purposes and does not include any authentication or authorization mechanisms. It is intended to be used as a starting point for building a RESTful API service.
