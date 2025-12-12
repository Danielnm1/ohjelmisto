class Auto:
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def __str__(self):
        return f"{self.__class__.__name__} {self.color} {self.weight}"
class Bike:
    def __init__(self,radius):
        self.radius = radius

class Motor(Auto,Bike):
    def __init__(self,color,weight,radius,speed):
        Auto.__init__(self,color,weight)
        Bike.__init__(self,radius)
        self.speed = speed
    def __str__(self):
        return f"{Auto.__str__(self)} {self.speed}"
m1 = Motor("red",25,15,210)
print(m1.radius)
print(m1.weight)
print(m1.speed)
print(m1.color)
print(m1.__str__())

