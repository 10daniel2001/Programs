# Funçao especifica para ler arquivos !
def read_file():
    with open("file_test.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
        print(f"Leitura de texto {texto}\n")

def write_escrita():
    with open("file_test.txt", "w", encoding="utf-8") as arquivo:
        entradas_inputes = input("Digite o texto para adcionar no arquivo \n")
        arquivo.write(entradas_inputes)
        print("Texto adicionado \n")
        print(entradas_inputes)

def acrescentar():
    with open("file_test.txt", "a", encoding="utf-8") as arquivo:
        acrecs = input("Digite para acrescentar\n")
        arquivo.write(acrecs)
        print(f"Texto acrescentado {acrecs}")

def atributos():
    with open("file_test.txt") as arquivo:
        arqui = arquivo
        print(arqui.name)
        print(arqui.mode)


def main():
    write_escrita()
    acrescentar()
    read_file()
    atributos()

if __name__=="__main__":
    main()