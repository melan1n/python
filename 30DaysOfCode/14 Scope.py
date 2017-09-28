class Difference:
   def __init__(self, a):
      self.__elements = a
      self.maximumDifference = 0
      self.elements = a


   def computeDifference(self):
       global maximumDifference
       maximumDifference = 0
       i = 0
       while i < len(a):
            for j in range((i + 1), len(a)):
                if self.maximumDifference < (abs(self.elements[i] - self.elements[j])):
                    self.maximumDifference = abs(self.elements[i] - self.elements[j])
            i = i + 1
       return maximumDifference
      
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)

d.computeDifference()

print(d.maximumDifference)

