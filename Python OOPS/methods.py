class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def display_info(self):
        print('Brand:', self.brand)
        print('Model:', self.model)
        print('Speed:', self.speed)

    def accelerate(self, amount):
        self.speed += amount

car1 = Car("Toyota", "Corolla", 120)
car1.display_info()
car1.accelerate(30) # Car.accelerate(car1, 30)
car1.display_info()