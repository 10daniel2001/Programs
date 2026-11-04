from pathlib import Path


class Manipular:

    def __init__(self, arquivo):
        self.arquivo = Path(__file__).parent / arquivo

    def abrir_arquivo(self):
        with open(self.arquivo, "r", encoding="utf-8") as arqq:
            conteudo = arqq.read()
            print(f"Conteúdo do arquivo: {conteudo}")


def main():
    objet = Manipular("arq.txt")
    objet.abrir_arquivo()


if __name__ == "__main__":
    main()