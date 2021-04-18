# Zvolené technologie

## Jádro

Jako programovací jazyk jsme zvolili Python.
Je populární a má velkou uživatelskou základnu,
netřeba říkat, že pro něj existuje spousta užitečných knihoven
(v době psaní tohoto dokumentu je jich na pypi.org k dispozici kolem 300 000).
Navíc s ním všichni z našeho týmu mají zkušenost.

Pro webový framework jsme zvolili Flask, jeden z hlavních frameworků pro vývoj webových aplikací v Pythonu.

## Uživatelské rozhraní

Pro generování webových stránek používáme templatovací engine Jinja2 jakožto výchozí engine, který Flask používá.
Uživatelské rozhraní se vykresluje ve webovém prohlížeči, na jeho popis je tedy využíváno HTML a CSS.

## Persistence dat

Jako databázový engine používáme PostgreSQL.
V kódu pak využíváme k přístupu k datům framework SQLAlchemy,
ten využívá model ...

TODO: jaký model?
zvolený způsob persistentního ukládání musí zajistit,
že se nikdy nebudou používat názvy tabulek a názvy jejich sloupečků v kódu jinde, než v datové vrstvě.

## Provázání balíčků/komponent

TODO: Flask-Injector
