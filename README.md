# djangox
Django backend, htmx frontend, mkdocs docs

`python -m venv .venv`

`source .venv bin activate`

`pip install --upgrade pip`

`pip install -r requirements.txt`

## docs

`cd docs ; mkdocs serve -a localhost:8001`

## client

`cd server ;python manage.py runserver`
`python manage.py migrate`

## remove pycache

`find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf`
