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
        super(Eletric_car, self).__init__(make,model,year)
        self.battery_size = 70
        self.remain_battery = 100
    def describe_battery(self):
        print('This car has {}-Kw/h battery size'.format(self.battery_size))
    
    def calc_autonomy(self):
        autonomy = ((self.battery_size * self.remain_battery)/100) * 6.13
        print('The autonomy is around {}Km'.format(autonomy))

    def update_batteryremain(self, remain):
        if remain >= 0 and remain <= 100:
            self.remain_battery = remain
            print('The ramain battery is now {}%'.format(self.remain_battery))
        else:
            print('Invalid remain battery')


my_tesla = Eletric_car("tesla","model s", 2018)
print(my_tesla.get_descriptive())
my_tesla.describe_battery()