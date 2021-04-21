class Bunch(dict):
   def __getattribute__(self, key):
       try: 
           return self[key]
       except KeyError:
           raise AttributeError(key)
   
   def __setattr__(self, key, value): 
       self[key] = value

items = [
    Bunch(Nazev='Svickova', Cena=123),
    Bunch(Nazev='Tika Masala', Cena=139),
    Bunch(Nazev='Kebab', Cena=99),
]

def get_items():
    return items