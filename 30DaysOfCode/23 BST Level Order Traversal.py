import sys

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
            return root

    def levelOrder(self,root):
        #Write your code here
        queue = []   #nodes
        levelOrder = ''  #string
        if root != None:
            queue.append(root)
            
            while queue != []:
                item = queue.pop() #node
                current = item   #node
                
                levelOrder += str(item.data) + ' '
                
                if current.left != None:
                    queue.insert(0, current.left)
                
                if current.right != None:
                    queue.insert(0, current.right)
                    
            print(levelOrder)   
            
            
        def __init__(self):
            self.levelOrder
            self.root
                    

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root,data)
myTree.levelOrder(root)

