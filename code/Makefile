all: debug

run:
	FLASK_APP=pl flask run

activate:
	. venv/bin/activate

install:
	python -m venv venv
	. venv/bin/activate
	python setup.py install

debug:
	FLASK_APP=pl FLASK_ENV=development FLASK_DEBUG=1 flask run
