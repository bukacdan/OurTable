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
	sudo -u postgres psql -c "CREATE DATABASE our_table;
	sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
	psql postgres -h 127.0.0.1 -d our_table -f dl/schema.sql
	psql -d our_table -a -f dl/Insert.sql
