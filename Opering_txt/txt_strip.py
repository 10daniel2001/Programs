
def contador_linha():
    with open("file_test.txt", "r") as arquivo:
        print("Total de linhas do arquivos")
        contador = 0
        for linh in arquivo:
            if linh:
                contador += 1
        print("Total = ", contador)


def function_strip():
    with open("file_test.txt", "r") as dfile:
        print("Total de linhas com o strip")
        contt = 0
        for flinh in dfile:
            if flinh.strip():
                contt += 1
        print("Cont strip = ", contt)

def main():
    with open("file_test.txt", "r") as arquivo:
        print("Representaçâo original da linha")
        for linha in arquivo:
            print(repr(linha))

    with open("file_test.txt", "r") as arqui:
        print("Representaçâo com o strip")
        for linha in arqui:
            linha_limpa = linha.strip()
            print(repr(linha_limpa))

    print("Chamando a funçâo \n")
    contador_linha()
    print("Chamando a funçâo com strip\n")
    function_strip()

if __name__=="__main__":
    main()