class Circle:
    radius = None
    circumference = None
    area = None

    def __init__(self, r):
        self.radius = r
        self.circumference = r * 3.14 * 2
        self.area = r * 3.14 * r



small_circle = Circle(3)
big_circle = Circle(15)

print(small_circle.area)
print(big_circle.area)
