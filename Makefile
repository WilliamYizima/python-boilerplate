generate-pylint-file:
	pylint --generate-rcfile > .pylintrc
install-pre-commit:
	pre-commit install
install:
	pip install -r requirements.txt
run:
	python -u run.py
# run-dev:
# 	uvicorn --proxy-headers  src.main.app:app --host 0.0.0.0 --port 9001
