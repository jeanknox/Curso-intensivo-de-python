class Cachorro:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade

    def sit(self):
        print(f"{self.name.title()} is now sitting!")

    def up(self):
        print(f"{self.name.title()} is now up!")

dog = Cachorro("bethoven",10)
dog.sit()
dog.up()
