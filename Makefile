linter:
	@echo "Run linters"
	black .
	isort .
	flake8 .
	pytest .

info:
	echo "Hello"
	@echo "Hello 2"
