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
- **Health Checks:** Includes ready-to-use `/health` and `/live` endpoints.
- **Testing:** Integrated testing with `pytest`.
- **Containerized:** Comes with a `Dockerfile` for easy building and deployment.
- **Quality Checks:** Integrated commands for type checking with `ty` and linting/formatting with `ruff`.

### Why Production-Ready?

The template is considered "production-ready" due to several key features that are essential for deploying, monitoring, and maintaining a service:

*   **Containerization:** The `Dockerfile` allows for building a consistent and isolated environment, which is a standard for reliable deployments.
*   **Externalized Configuration:** Using an `.env` file separates configuration from code, allowing for different settings in development, testing, and production.
*   **Monitoring & Health:** It includes structured logging and `/health` and `/live` endpoints, which are crucial for monitoring, debugging, and service orchestration (e.g., with Kubernetes).
*   **Testing:** The included testing framework allows for writing and running tests to ensure the application is working as expected.
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

2.  **Build and run the application:**
    Use the following command to build and run the Docker container.
    ```sh
    make start
    ```

The application will be available at `http://localhost:8000`. The health check endpoints are at `http://localhost:8000/health` and `http://localhost:8000/live`.

## 🛠️ Usage

This project uses `make` to streamline common tasks.

| Command      | Description                                                                       |
|--------------|-----------------------------------------------------------------------------------|
| `help`       | List all available commands.                                                      |
| `start`      | Build and run the Docker container in one go.                                     |
| `build`      | Build a Docker container named `fastapi-template`.                                |
| `run`        | Run the `fastapi-template` container with the source code mounted.                |
| `test`       | Run tests with `pytest`.                                                          |
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

Cross-Origin Resource Sharing (CORS) is configured via the `allowed_origins` setting in `src/app/config.py`. You can set this in your `.env` file as a comma-separated list of allowed origins.

**Example `.env` configuration:**
```sh
allowed_origins=http://localhost:3000,https://my-frontend.com
```
