install :
	pip install -r requirements.txt

lint:
	pylint sum.py

test :
	python -m pytest -vv test_sum.py