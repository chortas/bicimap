# -- Run scripts
.PHONY: install
install:
	python3 -m pip install --no-cache-dir -r requirements.txt

.PHONY: test
test:
	pytest -s app/tests/ --disable-pytest-warnings
