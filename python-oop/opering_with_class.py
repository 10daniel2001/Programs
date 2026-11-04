class Manipular:
    def __init__(self, aruivo):
        self.arquivo = aruivo


    def abrir_arquivo(self):
        with open(self.arquivo, "r", encoding="utf-8") as arqq:
            conteudo = arqq.read()
            print(f"Conteudo do arq {conteudo}")



def main():
    objet = Manipular("arq.txt")
    objet.abrir_arquivo()


    
