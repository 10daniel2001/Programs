def count_01():
    with open("count.txt", "r") as arquivo:
        texto = arquivo.read()
        contador = texto.count("dan")
        print("Total de dan é = ", contador)


count_01()