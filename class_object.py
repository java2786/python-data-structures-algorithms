class Employee:
    name = None
    salary = None
    bonus = None
    company = None
    # constructor
    def __init__(self, n, s, c):
        self.name = n
        self.salary = s
        self.company = c

    def addBonus(self):
        self.salary = self.salary * 1.05

obj1 = Employee("Keshu", 1500000, "google")
# obj1.fill_details("Keshu", 1500000)
# obj1.name = "Keshu"
# obj1.salary = 1500000

obj2 = Employee("Bharadwaj", 1200000, "Flipkart")
# obj2.name = "Bharadwaj"
# obj2.salary = 1500000
# obj2.fill_details("Bharadwaj", 1200000)

obj3 = Employee("Ansh", 1300000, "Amazon")
# obj3.fill_details("Ansh", 1300000)

print(obj1.salary)
print(obj2.salary)
print(obj3.salary)

print("==== giving bonus =====")
obj1.addBonus()
obj3.addBonus()

print(obj1.salary) 
input()
print(obj2.salary)
input()
print(obj3.salary)

