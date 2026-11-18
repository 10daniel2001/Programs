def count_01():
    with open("count.txt", "r") as arquivo:
        texto = arquivo.read()
        contador = texto.count("dan")
        print("Total de dan é = ", contador)


def count_02():
    with open("count_string.py", "r") as dfile:
        print("Procurando a palavra daniel")
        rtext = dfile.read()
        contar = rtext.split()
        print("Quantos daniel tem ?. É = ", contar)

count_01()
count_02()