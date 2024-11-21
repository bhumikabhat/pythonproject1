# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Porche",2025,"black",True)
car3 = Car("Ferrari",2025,"red", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
 
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car2.stop()
car3.describe()