run:
	python -m src.main "./data/despesas.csv"

test:
	python -m unittest discover -s tests

test_val:
	python -m unittest tests/test_validator.py