watch:
	pipenv run watchmedo shell-command \
      --patterns="a.py" \
      --command='pipenv run python a.py' \
      .

pep8:
	pipenv run isort a.py
	pipenv run black a.py --line-length 99