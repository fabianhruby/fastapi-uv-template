# FastAPI Template

This is a template for implementing APIs with FastAPI. The project includes the following components:

- **src/app/config.py**: Contains configuration settings for the FastAPI application.
- **src/app/main.py**: Main entry point for the app.
- **src/core/app.py**: Core application entry point where FastAPI App is created with health and live check endpoints.
- **src/core/routers/health.py**: Core router with health and live checks included.

## Getting Started

To build and run the Docker container, use the following commands:

```sh
make all
```

The application will be available at `http://localhost:8000`.

## Available Commands

- **help**: List all available commands
- **start**: Build and run the Docker container.
- **build**: Build a Docker container from the `Dockerfile` named `fastapi-template`.
- **run**: Run the Docker container named `fastapi-template` with the source code bound to the container.
- **check-ty**: Check the code inside the `/src` directory with `ty`.
- **check-ruff**: Check the code inside the `/src` directory with `ruff`.
- **check-all**: Check the code inside the `/src` directory with `ty` and `ruff`.

## Project Structure Guidelines

The code in the `/src/core` module should not be changed.   
It includes functionality that is common to every FastAPI project and should be reused. Custom implementations and additional features should live in the `/src/app/` directory.
