'''
important terminology:
- Attributes: variables
        make,color,miles
- Methods: funtions in class
    def go(self,mile):
- Constructor: initialization
    def __init__(self,make,color):
        self.make = make
        self.color = color
        self.miles = 0
- Instance: creating new instance
    car1 = Car('VW','Red')
    car2 = Car('BMW','Blue')
'''

class Car():

    def __init__(self,make,color):
        self.make = make
        self.color = color
        self.miles = 0


    def go(self,mile):
        self.miles += mile


car1 = Car('VW','Red')
car1.go(10)
print(f"car1 total mileage {car1.miles}")

car2 = Car('BMW','Blue')
car2.go(100)
print(f"car2 total mileage {car2.miles}")

car1.go(10) # adding up with last mileage value
print(f"car1 total mileage {car1.miles}")

car2.go(100) # adding up with last mileage value
print(f"car2 total mileage {car2.miles}")