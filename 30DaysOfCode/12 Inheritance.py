
class Person:
   def __init__(self, firstName, lastName, idNumber):
      self.firstName = firstName
      self.lastName = lastName
      self.idNumber = idNumber

   def printPerson(self):
      print("Name:", self.lastName + ",", self.firstName)
      print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    
        
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores=None):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self): #   Function Name: calculate     Return: A character denoting the grade.
        score_avg = sum(scores)/len(scores)
        if 90 <= score_avg <= 100:
            self.score_avg = 'O'
        elif 80 <= score_avg < 90:
            self.score_avg = 'E'
        elif 70 <= score_avg < 80:
            self.score_avg = 'A'
        elif 55 <= score_avg < 70:
            self.score_avg = 'P'
        elif 40 <= score_avg < 55:
            self.score_avg = 'D'
        elif score_avg < 40:
            self.score_avg = 'T'
        return self.score_avg

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
