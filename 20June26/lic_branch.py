class LICPolicy:
    def __init__(self, name):
        self.__holder_name = name
        self.__validity = 15
        self.__sum_assured = 200000

    # enCAPSULation - hide - private variable

    # display
    def display(self):
        print(f"Name: {self.__holder_name}")
        print(f"Validity: {self.__validity}")
        print(f"Sum Assured: {self.__sum_assured}")


    def set_validity(self, v):
        if(v>10):
            self.__validity = v
        