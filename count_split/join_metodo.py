from enum import show_flag_values


def  frase():
    texto = ["Lista", "De", "Compras", "Para o ano novo"]
    etxt = ', '.join(texto)

    with open("test_join.txt", "w") as file:
        file.write(etxt)

    print("\n")

    etct2 = "\n".join(texto)
    with open("test_join2.txt", "w") as dfile:
        dfile.write(etct2)

def main():
    frase()




if __name__=="__main__":
    main()
