
class Vehicle:
    def __init__(self, owner, city, reg_num):
        self.owner = owner
        self.city = city
        self.reg_num = reg_num

    def display(self):
        print(f"Owner: {self.owner}")
        print(f"City: {self.city}")
        print(f"Reg_num: {self.reg_num}")

# child of Vehicle, Vehicle is parent
class Car(Vehicle):
    def __init__(self, owner, city, reg_num, type):
        super().__init__(owner, city, reg_num)
        self.type = type 

    # def display(self):
    #     print(f"Owner: {self.owner}")
    #     print(f"City: {self.city}")
    #     print(f"Reg_num: {self.reg_num}")
    #     print(f"Type: {self.type}")




# car = Vehicle("4wheeler", "Ramesh", "Ghaziabad", "UP13AB7878")
# bike = Vehicle("2wheeler", "Mahesh", "Pune", "MH12JH8378")
# car1 = Vehicle("4wheeler", "Dinesh", "Delhi", "DL13DA7118")


car1 = Car("Ramesh", "Ghaziabad", "UP13AB7878", "Petrol")
car2 = Car("Dinesh", "Delhi", "DL13DA7118", "EV")
# bike = Vehicle("2wheeler", "Mahesh", "Pune", "MH12JH8378")

car1.display()


v = Vehicle("Dinesh", "punjab", "abc")
v.display()