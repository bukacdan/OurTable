all: debug

run:
	flask run

activate:
	. venv/bin/activate

install:
	python -m venv venv
	. venv/bin/activate
	python setup.py install

debug:
	FLASK_ENV=development FLASK_DEBUG=1 flask run
