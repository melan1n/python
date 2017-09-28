#Write your code here
'''Write a Calculator class with a single method: int power(int,int). The power method takes two integers, and , as parameters and returns the integer result of . If either or is negative, then the method must throw an exception with the message: n and p should be non-negative. '''

class Calculator:
    def __init__(self):
        self.Exception = 'n and p should be non-negative'
        
    def power(self, n, p):
        if n >= 0 and p >= 0:
            return n**p
        else:
            return self.Exception

myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
