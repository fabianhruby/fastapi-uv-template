# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync

# Expose port 8000
EXPOSE 8000

# Run the fastapi app
CMD ["/app/.venv/bin/fastapi", "run", "src/app/main.py", "--reload", "--host", "0.0.0.0", "--port", "8000"]
