# FastAPI Template

This is a template for implementing APIs with FastAPI. The project includes the following components:

- **src/app/config.py**: Contains configuration settings for the FastAPI application.
- **src/app/main.py**: Main entry point for the app.
- **src/core/app.py**: Core application entry point where FastAPI App is created with health and live check endpoints.
- **src/core/routers/health.py**: Core router with health and live checks included.
- **src/core/logging.py**: Configuration for logging based on the stage.
- **src/core/middleware/logging.py**: Logging middleware to log request and response details.

## Getting Started

To build and run the Docker container, use the following commands:

```sh
make run
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

## Logging Middleware

The logging middleware is configured based on the `stage` variable in the `.env` file. The available stages are:

- **local**: DEBUG level logging
- **dev**: INFO level logging
- **test**: WARNING level logging
- **prod**: INFO level logging

To configure the logging, set the `stage` variable in the `.env` file to one of the above values. For example:

```sh
stage=local
````

This will enable DEBUG level logging for the application.
