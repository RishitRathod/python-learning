class Vehicle:
    def _init_(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
    def show_details(self):
        print("\n Vehicle")
        print("Mileage of Vehicle is ", self.mileage)
        print("Cost of Vehicle is ",self.cost)

v1 = Vehicle(50,500)
v1.show_details()


# # creating child class
class Car(Vehicle):
    def show_car(self):
        print("\n Car")
# Instantiating the object for child class
c1 = Car(20,20000)
c1.show_details()
# invoking the child class method
c1.show_car()