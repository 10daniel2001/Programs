"Nossa super class se chama polymorphism"

#Super class
class Polymorphism:
    def __init__(self, name, age, is_id):
        self.name = name
        self.is_id = is_id
        self.age = age

        "Nada esta privado, uma observaçao"

    # Method the super class
    def print_id(self):
        print(f"Your ID is - {self.is_id}")
    #Method the super class
    def your_Age(self):
        print(f"Your age is {self.age}")

#Sub class
class Child(Polymorphism):
    def __init__(self, name, age, ident):
        # Call the parent class constructor, passing the required arguments
        super().__init__(name, age, is_id=ident)
        self.age = age
    # super() é uma função que dá acesso aos métodos da classe pai (super class)
    # de dentro da classe filha (subclass). É assim que a classe filha "herda" e
    # reaproveita o comportamento já definido na classe pai, sem precisar reescrever tudo.

    def print_id(self):
        print(f"Is Id {self.is_id * 2}")
        #Outro comportamento pois id multiplica com 2

def main():
    peaple_dad = Polymorphism("david", 49, 2011)

    childd = Child("Andre", 25, 2025)

    childd.print_id()
    childd.your_Age()


if __name__=="__main__":
    main()