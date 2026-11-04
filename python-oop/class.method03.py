"Nossa classe Carro representa um carro com atributos de marca, modelo e ano."
"O método display_info retorna uma string formatada com essas informações."

"this Car class represents a car with attributes for make, model, and year."
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    #Methods are actions that can be performed by objects of a class. 
    #They define the behavior of the objects and can access and modify 
    #the attributes of the class.

    #metodos são ações que podem ser realizadas por objetos de uma classe.
    #Eles definem o comportamento dos objetos e podem acessar e modificar
    #os atributos da classe.