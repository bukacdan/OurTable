all: debug

run:
	FLASK_APP=pl flask run

activate:
	. venv/bin/activate

install:
	python -m venv venv
	. venv/bin/activate
<<<<<<< HEAD
	pip install -r requirements.txt
=======
	python setup.py install
postgres:
	source venv/bin/activate
	sudo apt-get install postgresql postgresql-client
>>>>>>> 4eacc9f (Modified schema.sql, Makefile finished, db.py first few functions)

	pipenv install flask-alchemy

createdb:
	createdb our_table
	psql postgres -h 127.0.0.1 -d our_table -f app/schema.sql
debug:
	FLASK_APP=pl FLASK_ENV=development FLASK_DEBUG=1 flask run
