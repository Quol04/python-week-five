# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️)

    
 # Define the class car      
class Car:
    def move(self):
        return "Driving on land oo!"
# Define the class plane
class Plane:
    def move(self):
        return "Soaring in the sky,dammit!"

# Polymorphism being applied here
for vehicle in [Car(), Plane()]:
    print(vehicle.move())        