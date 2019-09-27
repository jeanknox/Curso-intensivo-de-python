class Cachorro:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade

    def sit(self):
        print(f"{self.name.title()} is now sitting!")

    def up(self):
        print(f"{self.name.title()} is now up!")

dog = Cachorro("bethoven",10)
dog1 = Cachorro("batatinha",5)

print(f"O nome do meu cachorro e:{dog.name}e tem :{dog.idade} anos")

print(f"O nome do meu cachorro e:{dog1.name}e tem :{dog1.idade} anos")
