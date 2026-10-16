# Funçao especifica para ler arquivos !
def read_file():
    with open("file_test.txt", "r", encoding="utf-8") as arquivo:
        arquivo.read()

def write_escrita():
    with open("file_test.txt", "w", encoding="utf-8") as arquivo:
        entradas_inputes = input("Digite o texto para adcionar no arquivo \n")
        arquivo.write(entradas_inputes)
        print("Texto adicionado \n")
        print(entradas_inputes)
