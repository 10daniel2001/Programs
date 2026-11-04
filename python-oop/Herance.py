#Super class
class Herance:
    def __init__(self, name, age, year):
        self._name = name
        self._age = age
        self.year = year
        #Definindo atriburos de classe para instaciar objetos

    def verificarIdade(self):
        if self._age >= 18:
            print("Você é maior de idade")
        else:
            print("Você é menor de idade")

# Sub class
class Filha(Herance):

    #Aqui onde a Subclass pega todos os mesmo conceitos de atributos da Super class
    #Onde a herança da class pai passa a copia dos atributos para a filha
    #Mas tem a opçao de criar proprios atributos para a class filha, como lá esta city
    def __init__(self, name, age, year, city):
        super().__init__(name, age, year)
        self.city = city

    def imprimir(self):
        print(f"Sua cidade e {self.city}")

def main():

    pai = Herance("Carlos", 25, 2026)
    #Obejto da super class istaciado

    filha = Filha("Daniel", 20, 2021, "Goiania Go")
    #Objeto da subclass istanciado

    "Aqui os metodos das class seram chamados"
    pai.verificarIdade()
    filha.imprimir()
    "Nao ha poliformismo neste codigo pois e um exemplo de Herança"

if __name__=="__main__":
    main()

    #A saida sera simples apenas para uso didatico
    "Vocề maior de idade"
    "Sua cidade e Goiania Go"

