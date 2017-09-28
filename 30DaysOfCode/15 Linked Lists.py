class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class Solution:
   def display(self, head):
       current = head
       while current:
            print(current.data,end=' ')
            current = current.next

   def __init__(self):
        self.head = None
        self.size = 0

   def insert(self,head,data):
       if head == None:
          self.size += 1
          new_node = Node (data)
          new_node.next = self.head
          self.head = new_node
          
       else:
          new_node = Node(data)  
          current_node = self.head  
          while (current_node.next):
             current_node = current_node.next
          self.size += 1
          current_node.next = new_node

       return self.head    

      
mylist = Solution()
T = int(input())
head = None
for i in range(T):
   data = int(input())
   head = mylist.insert(head, data)
mylist.display(head);
