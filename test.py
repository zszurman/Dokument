x = {'ona': 'jola', 'on': 'zbyszek', 'dx': 2}
print(f"{x['ona'].title()} i {x['on'].upper()} to {x['dx']}")
print(x)
x['ona'] = 'Tosia'
x['dx'] *= 2
x['on'] = 'Szymek'
print(f"{x['ona'].upper()} i {x['on'].lower()} to {x['dx']}\n\n")

for i in x.keys():
    print(i)

print(f"\n")

for i in x.values():
    print(i)
tekst = ""
for i, j in x.items():
    tekst += f"Klucz: {i}, Wartość: {j} "
print(f"{tekst}\n")

tekst = ""
del x['dx']
for i in sorted(x.values()):
    tekst += f"{i} i "
print(f"{tekst}\n")

tekst = ""

for i in x.values():
    tekst += f"{i} i "
print(tekst)


def make_krotka(*stokrotka):
    return stokrotka


krotka = make_krotka('kk', 'ggg', 'ohjoy')
print(krotka)
