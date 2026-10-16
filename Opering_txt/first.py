# Funçao especifica para ler arquivos !
def read_file():
    with open("file_test.txt", "r", encoding="utf-8") as arquivo:
        arquivo.read()