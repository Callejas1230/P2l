#class Punto:
 #   x = 0
  #  y = 0
#def SetX(self, x):
 #   self.x = x
#def setY(self, y):
 #   self.y = y
#def getX(self):
 #   return self.x
#def getY(self):
 #   return self.y
#def __eq__(self, o):
 #   return self.x == o.x and self.y == o.y
#def __str__(self):
 #   return "({}, {})".format(self.x, self.y)
#p1 = Punto()
#p2 = Punto()
#p1.setX(1)
#p1.setY(2)
#p2.setX(3)
#p2.setY(4)
#print(p1)
#print(p2)
#if p1 == p2:
 #   print("Son iguales")
#else:
 #   print("Son distintos")



import math

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return [self.x, self.y]

    def coord_polares(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        return [r, theta]

    def __str__(self):
        return f'Punto(x={self.x}, y={self.y})'
