class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def login(self):
        print(f"{self.first_name} is now logged")
    def logout(self):
        print(f"{self.first_name} is now logged out")
    def say_hello(self):
        print("Ola {}".format(self.first_name))

usuario = User("jean","marcio")
usuario.login()
usuario.logout()
usuario.say_hello()
