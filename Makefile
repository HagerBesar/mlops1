install :
	pip install -r requirement.txt

lint:
	pylint sum.py

test :
	python -m pytest -vv test_sum.py