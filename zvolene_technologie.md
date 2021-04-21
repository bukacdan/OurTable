# Zvolené technologie

## Jádro

Jako programovací jazyk jsme zvolili Python. Je populární a má velkou
uživatelskou základnu, netřeba říkat, že pro něj existuje spousta užitečných
knihoven (v době psaní tohoto dokumentu je jich na pypi.org k dispozici kolem
300 000). Navíc s ním všichni z našeho týmu mají zkušenost.

Pro webový framework jsme zvolili Flask, jeden z hlavních frameworků pro vývoj
webových aplikací v Pythonu. Naše aplikace využívá relaxovanou třívrstvou
architekturu.

## Uživatelské rozhraní

Pro generování webových stránek používáme templatovací engine Jinja2 jakožto
výchozí engine, který Flask používá. Uživatelské rozhraní se vykresluje ve
webovém prohlížeči, na jeho popis je tedy využíváno HTML a CSS (a trocha
javascriptu). CSS se generuje automaticky ze SASS souborů, na to využíváme
knihovnu libsass.

## Persistence dat

Jako databázový engine používáme PostgreSQL. V kódu pak využíváme pro přístup k
datům framework SQLAlchemy. Ten pro mapování databáze na třídy využívá vzor Data
Mapper.

## Provázání balíčků/komponent

K provázání balíčků využíváme Flask-Injector, což je plugin frameworku Flask.
Provázání zajišťuje, že controllery v prezentační vrstvě se mohou odkazovat
na rozhraní mapperů (což je abstraktní třída). K tomu, abychom zajistili
abstraktnost třídy v Pythonu využíváme balíček ABC (abstract base class), který
je součástí pythonu samotného. Samotná logika je pak implementovaná pomocí tříd
v databázové vrstvě.
