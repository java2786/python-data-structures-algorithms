class Patient:
    def __init__(self, name, age, bloodGroup):
        self.name = name
        self.age = age
        self.bloodGroup = bloodGroup
        self.doctorAssigned = None

    def showDetails(self):
        print(f"Name: {self.name}, Age: {self.age}, BG: {self.bloodGroup}, Doctor: {self.doctorAssigned}")


p1 = Patient("Ramesh", 82, 'A+')
p2 = Patient("Mahesh", 83, 'A-')

p1.showDetails()
p2.showDetails()
