from datetime import datetime


nomes = ["Carlos", "Daniel", "Godoi"]

for li in nomes:
    my_names = f"Nomes {li:12} - Numero de letras {len(li): 3d}"
    print(my_names)

print()

pi = 3.1415
my_number = f"Numero de PI é {pi:.1f}"
deslocado = f"Numero PI deslocado é {pi:6.1f}"
number_preci = f"Numero PI preciso é {pi:.4f}"

print(my_number)
print(deslocado)
print(number_preci)

print()

data = datetime.now()
my_date = f"A data de hoje é {data}"
print(data)
