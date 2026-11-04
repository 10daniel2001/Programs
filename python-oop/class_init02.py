"Vamos entender o que é a inicialização de classes em Python. A inicialização de uma classe"
"é o processo pelo qual uma nova instância da classe é criada e configurada. Isso geralmente "
"envolve a definição de atributos e a execução de qualquer lógica necessária para preparar o "
"objeto para uso."
"Em Python, a inicialização de uma classe é feita através do método especial `__init__" 

"Go understand what class initialization is in Python. Class initialization is the process by "
"which a new instance of the class is created and configured. This usually involves defining "
"attributes and executing any necessary logic to prepare the object for use. In Python, "
"class initialization is done through the special method `__init__`."

class Car:
    #Self e um parâmetro especial que representa a instância atual da classe.
    #Ele é usado para acessar variáveis e métodos pertencentes à classe.

    #self is a special parameter that represents the current instance of the class.
    #It is used to access variables and methods belonging to the class.

    def __init__(self, make, model, year):
        # Initialize the attributes of the class
        # Icialize os atributos da classe
        self.make = make
        self.model = model
        self.year = year

    def display_info(self): #metodo para exibir informações sobre o carro
                            #method to display information about the car
        return f"{self.year} {self.make} {self.model}"