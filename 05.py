class Car():
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
            ("You cant rollback this odometer mtf")

    def increase_odometer(self,miles):
        self.odometer += miles

    class Eletric_car(Car):
        def __init__(self,make, model, year):
            super(Eletric_car,self).__init__(make,model,year)


    my_tesla = Eletric_car("tesla","model s", 2018)

    print(my_tesla.get_descriptive())
