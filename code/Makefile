all: debug

run:
	FLASK_APP=pl flask run

activate:
	. venv/bin/activate

install:
	python -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt

debug:
	FLASK_APP=pl FLASK_ENV=development FLASK_DEBUG=1 flask run

postgres:
	sudo apt-get install postgresql postgresql-client

createdb:
	createdb our_table
	psql postgres -h 127.0.0.1 -d our_table -f app/schema.sql
