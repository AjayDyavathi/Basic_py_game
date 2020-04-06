import math

class vector(object):
    def __init__(self, list1, list2):
        self.diff = (list2[0]-list1[0],list2[1]-list1[1])
        print (self.diff)

    def distance(self):
        self.a = self.diff[0]
        self.b = self.diff[1]
        return math.sqrt(self.a**2+self.b**2)

    def unit(self):
        distance = self.distance()
        self.aunit = self.a/distance
        self.bunit = self.b/distance
        return self.aunit, self.bunit


a=(20.0,35.0)
b=(10.0,15.0)

thing = vector(a,b)
print (thing.distance())
print (thing.unit())
