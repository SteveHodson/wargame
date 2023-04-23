activate = . .venv/bin/activate

.PHONY: tests

.venv: .venv/touchfile

.venv/touchfile: requirements.txt
	test -d .venv || python3 -m venv .venv
	$(activate); pip install -Ur requirements.txt
	touch .venv/touchfile

tests:
	$(activate); python3 -m pytest

wargame:
	$(activate); python3 src/battle.py

tag:
	@git tag $(TAG)
	@git push --tags

clean:
	@echo 'Cleaning generated files'
	@rm -rf .venv
	@find . -type d -iname "__pycache__" -exec rm -rf "{}" +
	@find . -type d -iname ".pytest_cache" -exec rm -rf "{}" +
