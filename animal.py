# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️)

# Define the base class Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving"
    
        
        