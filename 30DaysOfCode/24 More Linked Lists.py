class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class Solution:
   def insert(self,head,data):
       p = Node(data) #initialize a node
       if head == None:
          head = p  #if no head exists set node as head
       elif head.next == None: 
          head.next = p #if second node does not exist place node as second
       else:
          start = head   #set a variable for current node 
          while(start.next != None):
             start = start.next  #move current node until pointer to next node is NULL
          start.next = p  #place node as next
       return head
      
   def display(self, head):
       current = head
       while current:
            print(current.data,end=' ')
            current = current.next
   def removeDuplicates(self,head):                
        tmp = head
        while tmp.next != None:                     #loop until last node
            next_node = tmp.next                    #set next node
            second_next_node = next_node.next       #set second next node
            
            if next_node.data == tmp.data:
                tmp.next = second_next_node         #move pointer of current
                                                
            else:
                tmp = tmp.next
        
        return head                                 #head of result linked list
                
mylist = Solution()
T = int(input())
head = None
for i in range(T):
   data = int(input())
   head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head);
