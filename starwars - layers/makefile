.DEFAULT_GOAL := build

build:
	docker build -t my-flask-app .
.PHONY: build

run:
	docker run -p 3008:3008 my-flask-app
.PHONY: run
