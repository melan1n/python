from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
   def __init__(self, title, author):
      self.title = title
      self.author = author
   @abstractmethod
   def display(): pass
   
#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price
    
    def display(self):
        print('Title:' + ' ' + title)
        print('Author:' + ' ' + author)
        print('Price:' + ' ' + str(price))
        
'''    Inherits from Book
    Has a parameterized constructor taking these parameters:
      Title  string
      Author  string
      Price  int 
    Implements the Book class' abstract display() method so it prints these lines:
        Title:, a space, and then the current instance's Title.
        Author, a space, and then the current instance's Author.
        Price, a space, and then the current instance's Price.
'''

title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
