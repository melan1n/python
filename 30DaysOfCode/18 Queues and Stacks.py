class Solution:
    # Write your code here
    '''
    Two instance variables: one for your STACK, and one for your QUEUE.
    A void pushCharacter(char ch) method that pushes a character onto a stack.
    A void enqueueCharacter(char ch) method that enqueues a character in the QUEUE instance variable.
    A char popCharacter() method that pops and returns the character at the top of the STACK instance variable.
    A char dequeueCharacter() method that dequeues and returns the first character in the QUEUE instance variable.
'''
    def __init__(self):
        self.stack = []
        self.queue = []
        
    def pushCharacter(self, char):   #yes
        self.stack.append(char)
    
    def enqueueCharacter(self, char): #sey
        self.queue.insert(0, char)
                
    def popCharacter(self):   #s
        item = self.stack.pop(-1)
        return item
    
    def dequeueCharacter(self): #y
        item = self.queue.pop(-1)
        return item
        

s = input()
obj = Solution()
l = len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

for i in range(1//2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")

