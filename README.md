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

OR by default

`export PYTHONDONTWRITEBYTECODE=1` into .bashrc or .zshrc

## remove DS_store

`find . | grep -E "(/__pycache__$|\.DS_Store|\.pyo$)" | xargs rm -rf`

OR by default

`defaults write com.apple.desktopservices DSDontWriteNetworkStores true`
