
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


if __name__=="__main__":
    main()