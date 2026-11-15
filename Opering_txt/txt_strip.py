
def main():
    with open("file_test.txt", "r") as arquivo:
        print("Reprsentaçâo original da linha")
        for linha in arquivo:
            print(repr(linha))

    with open("file_test.txt", "rb") as arqui:
        print("Representaçâo com os strip")
        for linha in arqui:
            linha_limpa = linha.strip()
            print(repr(linha_limpa))













if __name__=="__main__":
    main()