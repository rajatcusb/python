class Car:
    total_cars = 0

    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        self.is_running = False
        Car.total_cars += 1

    def start(self):
        if not self.is_running:
            self.is_running = True
            return "Car is now running."
        else:
            return "Car is already running."

    def stop(self):
        if self.is_running:
            self.is_running = False
            return "Car has been stopped."
        else:
            return "Car is already stopped."

    def accelerate(self):
        if self.is_running:
            return "Car is accelerating."
        else:
            return "Car must be started to accelerate."

    @staticmethod
    def count_cars():
        return f"Total number of cars created: {Car.total_cars}"

# Create some Car instances
car1 = Car("Honda Civic", "Silver", 25000)
car2 = Car("Toyota Corolla", "Blue", 22000)

# Interact with the cars
print(car1.start())
print(car2.start())
print(car1.accelerate())
print(car2.accelerate())
print(car1.stop())
print(car2.stop())

# Count the total number of cars
print(Car.count_cars())
