class Car:
    def __init__(self, make, model, year, odometer = 0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def get_descriptive(self):
        name_long = self.make +" "+ self.model +" "+ str(self.year)
        return name_long

    def get_odometer(self):
        print("This cars have {} miles".format(self.odometer))

    def update_odometer(self,miles):
        if miles >= self.odometer:
            self.odometer = miles
        else:
            print("You cant rollback this odometer mtf")
    def increase_odometer(self,miles):
        self.odometer += miles

carro = Car("Vw","fusca",1987)
print(carro.get_descriptive())
carro.update_odometer(10000)
carro.get_odometer()
carro.update_odometer(1000)
carro.increase_odometer(100)
carro.get_odometer()
