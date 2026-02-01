help:
	@echo	"Available commands:"
	@echo	"start		- Build and run the docker container"
	@echo	"build		- Build a docker container from the Dockerfile named fastapi-template"
	@echo	"run		- Run the docker container named fastapi-template with binding the source code to the container"
	@echo	"check-ty	- Check the code inside the /src directory with ty (https://docs.astral.sh/ty/)"
	@echo	"check-ruff	- Check the code inside the /src directory with ruff (https://docs.astral.sh/ruff/)"
	@echo	"check-all	- Check the code inside the /src directory with ty and ruff"
	@echo	""

start:
	make build
	make run

build:
	docker build -t fastapi-template .

run:
	docker run -p 8000:8000 --mount type=bind,source=./src,target=/app/src fastapi-template

check-ty:
	ty check src/

check-ruff:
	ruff check src/

check-all:
	make check-ty
	make check-ruff
