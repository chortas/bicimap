# -- Run scripts
.PHONY: install
install:
	python3 -m pip install --no-cache-dir -r requirements.txt

.PHONY: test
test:
	pytest -s app/tests/ --disable-pytest-warnings

HEROKU_APP_NAME := bicimap

# -- Heroku related commands
# You need to be logged in Heroku CLI before doing this
#   heroku login
#   heroku container:login
.PHONY: heroku-push
heroku-push:
	heroku container:push web --recursive --app=$(HEROKU_APP_NAME) --verbose

.PHONY: heroku-release
heroku-release:
	heroku container:release web --app $(HEROKU_APP_NAME) --verbose
