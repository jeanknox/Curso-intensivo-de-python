class Restaurant:
    def __init__(self, restaurant_name, cuisinetype):
        self.restaurant_name = restaurant_name
        self.cuisinetype = cuisinetype
    def describe_restaurant(self):
        print(f"O nome do restaurante e: {self.restaurant_name}")
        print(f"O tipo de cozinha e: {self.cuisinetype}")
    def open_restaurant(self):
        print("O restaurante: {self.restaurant_name} is now open")

restaurant = Restaurant("ikone","comida japonesa")
print(restaurant.restaurant_name)
print(restaurant.cuisinetype)
restaurant.describe_restaurant()
