# Rezervační systém OurTable

Webová aplikace pro on-line rezervování stolů v restauraci.
Hosté si mohou vytvořit rezervaci v restauraci bez nutnosti telefonovat.
Personálu aplikace umožňuje kontrolu nad aktuálními rezervacemi, případné omezení rezervací z důvodu kapacity nebo změněné otevírací doby restaurace.

- [1. Iterace](https://gitlab.fit.cvut.cz/rencjaku/bi-si2021/tree/iterace/01)
- [2. Iterace](https://gitlab.fit.cvut.cz/rencjaku/bi-si2021/tree/iterace/02)
- [3. Iterace](https://gitlab.fit.cvut.cz/rencjaku/bi-si2021/tree/iterace/03)

## Instalační příručka

Veškeré instalování závislostí, inicializace databáze i spouštění aplikace je realizováno pomocí [Makefile](./code/Makefile).  
Ten obsahuje targety níže, každý z nich lze spustit pomocí `make <target>`.

- **all**: spustí aplikaci v debug (vývojářské) konfiguraci
- **run**: spustí aplikaci v produkční konfiguraci
- **activate**: aktivuje virtuální python environment
- **debug**: spustí aplikaci v debug (vývojářské) konfiguraci
- **postgres**: nainstaluje do virtuálního environmentu všechny potřebné závislosti k postgress databázi
- **createdb**: vytvoří databázi _(heslo pro uživatele postgres je "postgres")_, a vloží do ní data

### První spuštění

1. `make install` - vytvoří virtuální environment a nainstaluje do něja závislosti
2. `make postgres` - nainstaluje databázi
3. `make createdb` - inicializuje databázi
4. `make all` - spustí aplikaci

### Následná spuštění

- `make all` - spustí aplikaci

## Dokumentace

- [html dokumentace ze zdrojových kódů](./documentation/code_documentation/_build/html/index.html)
- [textová dokumentace k architektuře aplikace](./documentation/architecture_documentation)

## Členové

|     Jméno      | 1. iterace | 2. iterace | 3.iterace |
| :------------: | :--------: | :--------: | :-------: |
|  Bukač Daniel  |     0      |     0      |     0     |
| Szkandera Jiří |     0      |     0      |     0     |
|   Renc Jakub   |     0      |     0      |     0     |
| Hývnar Ondřej  |     0      |     0      |     0     |

## Změny oproti 2. iteraci

- Opravili jsme využití table mapper vzoru v `bl/services/reservation.py` (v druhé iteraci byl porušen).
