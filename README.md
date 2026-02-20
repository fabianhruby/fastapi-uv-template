# 🚀 FastAPI UV Template 🚀

![Python Version](https://img.shields.io/badge/python-3.14-blue)
![Framework](https://img.shields.io/badge/framework-FastAPI-green)
![Code Style](https://img.shields.io/badge/code%20style-ruff-black)

A production-ready template for building high-performance APIs with FastAPI, using `uv` for lightning-fast dependency management.

## ✨ Features

- **High Performance:** Built on [FastAPI](https://fastapi.tiangolo.com/) and Uvicorn.
- **Blazing Fast Toolkit:** Uses `uv` for dependency management and `ruff` for linting, both from [Astral](https://astral.sh/).
- **Structured Logging:** Centralized and configurable logging setup.
- **Insightful Middleware:** Log requests and responses for better debugging.
- **CORS:** Pre-configured Cross-Origin Resource Sharing (CORS) middleware.
- **Rate Limiting:** Protects your API with a flexible, Redis-based rate limiter.
- **Health Checks:** Includes ready-to-use `/health` and `/live` endpoints.
- **Testing:** Integrated testing with `pytest` and `pytest-docker` for seamless service testing.
- **Containerized:** Comes with a `Dockerfile` for easy building and deployment, and `docker-compose.yml` for multi-service local development.
- **Quality Checks:** Integrated commands for type checking with `ty` and linting/formatting with `ruff`.

### Why Production-Ready?

The template is considered "production-ready" due to several key features that are essential for deploying, monitoring, and maintaining a service:

*   **Containerization:** The `Dockerfile` allows for building a consistent and isolated environment, which is a standard for reliable deployments. `docker-compose.yml` simplifies multi-service development.
*   **Externalized Configuration:** Using an `.env` file separates configuration from code, allowing for different settings in development, testing, and production.
*   **Monitoring & Health:** It includes structured logging and `/health` and `/live` endpoints, which are crucial for monitoring, debugging, and service orchestration (e.g., with Kubernetes).
*   **Testing:** The included testing framework allows for writing and running tests to ensure the application is working as expected, with `pytest-docker` handling external service dependencies.
*   **Scalable Architecture:** The separation of `src/app` (application logic) and `src/core` (reusable boilerplate) provides a clean architecture that is easy to maintain and scale.
*   **Code Quality Enforcement:** Integrated linting and type checking help ensure code quality and prevent bugs, which is vital for a stable production application.

## ✅ Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Make](https://www.gnu.org/software/make/)

## 🚀 Getting Started

1.  **Set up your environment variables:**
    Copy the template file to create your local environment configuration.
    ```sh
    cp .env.template .env
    ```
    You can then edit the `.env` file to change the `stage` or other settings.

2.  **Start the application and its services (Redis):**
    Use the following command to build and run the FastAPI application and the Redis database using Docker Compose.
    ```sh
    make up
    ```
    This will start the `fastapi` service and the `redis` service in detached mode.

3.  **Access the application:**
    The application will be available at `http://localhost:8000`. The health check endpoints are at `http://localhost:8000/health` and `http://localhost:8000/live`.

## 🛠️ Usage

This project uses `make` to streamline common tasks.

| Command      | Description                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `help`       | List all available commands.                                                      |
| `up`         | Start the Docker Compose services (fastapi and redis) in detached mode.               |
| `down`       | Stop and remove the Docker Compose services.                                      |
| `logs`       | View real-time logs from the Docker Compose services.                             |
| `test`       | Run tests with `pytest`. A temporary Redis container will be managed by `pytest-docker` for tests. |
| `check-ty`   | Check the code in the `/src` directory with `ty`.                                 |
| `check-ruff` | Check the code in the `/src` directory with `ruff`.                               |
| `check-all`  | Run both `check-ty` and `check-ruff`.                                             |


## 📂 Project Structure

The project is organized into two main directories: `src/app` and `src/core`.

-   `src/app/`: This is where your custom application logic lives.
    -   `api/`: API endpoints (routers).
    -   `data/`: Data models and schemas (e.g., Pydantic models).
    -   `services/`: Business logic.
    -   `interfaces/`: Interfaces to external services or databases.
    -   `config.py`: Application-specific configuration.
    -   `main.py`: Main application entry point.

-   `src/core/`: This is the core, reusable boilerplate. **You should generally not need to modify the code in this directory.**
    -   `app.py`: FastAPI app creation with core middleware and routers.
    -   `logging.py`: Logging configuration.
    -   `middleware/`: Core middleware.
    -   `routers/`: Core routers, including health checks.

## ✍️ Extending the API with Custom Routers

To add your own API endpoints and logic:

1.  **Create a new router file:** Inside `src/app/api/`, create a new Python file (e.g., `my_router.py`).
    Define your FastAPI router and endpoints within this file:

    ```python
    from fastapi import APIRouter

    router = APIRouter()

    @router.get("/my-endpoint")
    async def read_my_endpoint():
        return {"message": "Hello from my custom endpoint!"}
    ```

2.  **Include the router in `main.py`:** Open `src/app/main.py` and import your new router.
    Then, include it in the main FastAPI application using `app.include_router()`.

    ```python
    # src/app/main.py
    """Main entry point for the app."""

    from fastapi import FastAPI

    from core.app import create_app
    from .config import settings

    # Import your new router
    from .api.my_router import router as my_custom_router

    # The app is created by the core module
    app: FastAPI = create_app(settings=settings)

    # Include your custom routers here
    app.include_router(my_custom_router, prefix="/api/v1", tags=["example"])
    ```
    This example includes `my_custom_router` with a `/api/v1` prefix and a "example" tag, which will organize it nicely in the automatically generated OpenAPI documentation (`/docs`).

## ⚙️ Configuration

### Logging

Logging is configured by the `STAGE` setting in `.env`, using the mapping defined in `src/core/logging.py`. The root logger format includes timestamp, level, name and message. Uvicorn access logs are suppressed to WARNING.

The available stages and corresponding log levels are:
- `local`: DEBUG
- `dev`: INFO
- `test`: WARNING
- `prod`: INFO

**Example `.env` configuration:**
```sh
STAGE=local
```

### CORS

CORS settings are loaded from `src/app/config.py`. The `CORSSettings` model pulls values prefixed with `CORS_` from the environment. In `src/core/app.py`, these values are passed directly to FastAPI’s `CORSMiddleware`.

Environment variables (prefixed with `CORS_`) can be set in `.env`:
- `CORS_ALLOW_ORIGINS` – comma‑separated list of allowed origins, default `*`
- `CORS_ALLOW_CREDENTIALS` – boolean, default `true`
- `CORS_ALLOW_METHODS` – comma‑separated list of allowed methods, default `*`
- `CORS_ALLOW_HEADERS` – comma‑separated list of allowed headers, default `*`

```sh
CORS_ALLOW_ORIGINS=http://localhost:5000,https://my-frontend.com
CORS_ALLOW_CREDENTIALS=true
CORS_ALLOW_METHODS=GET,POST,PUT,DELETE
CORS_ALLOW_HEADERS=Authorization,Content-Type
```

### Rate Limiting

The application includes a middleware for rate limiting to protect your API from excessive traffic. It uses a fixed-window algorithm implemented with Redis.

Rate limiting settings are loaded from `src/app/config.py`. The `RateLimitingSettings` model pulls values prefixed with `RATE_LIMITING_` from the environment, and `RedisSettings` uses the `REDIS_` prefix.

When using `docker-compose.yml` for development, the `REDIS_URL` for the `web` service will automatically be set to `redis://redis:6379/0` to connect to the `redis` service. For local development outside of Docker Compose, `REDIS_URL` defaults to `redis://localhost:6379/0`.

Environment variables can be set in `.env`:
- `REDIS_URL` – The connection URL for your Redis instance (e.g., `redis://localhost:6379/0`).
- `RATE_LIMITING_DEFAULT_LIMIT` – The default number of requests allowed in a time window for an IP address, default `100`.
- `RATE_LIMITING_WINDOW_SECONDS` – The duration of the time window in seconds, default `3600` (1 hour).
- `RATE_LIMITING_PATH_LIMITS` – A JSON string defining an array of path-specific limits. Each object in the array must contain `path`, `limit`, and `window_seconds`.

**Example `.env` configuration:**
```sh
REDIS_URL=redis://localhost:6379/0 # Used for local, non-Docker Compose development
RATE_LIMITING_DEFAULT_LIMIT=200
RATE_LIMITING_WINDOW_SECONDS=60
RATE_LIMITING_PATH_LIMITS='[{"path": "/health", "limit": 10, "window_seconds": 60}, {"path": "/live", "limit": 10, "window_seconds": 60}]'
```
