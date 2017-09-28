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

    def getHeight(self,root):
             
        if root == None:
            return -1
                
        else:
            height_left = self.getHeight(root.left)
            height_right = self.getHeight(root.right)        
            return max(height_left, height_right) + 1
         

    def __init__(self):
        self.getHeight

T = int(input())

myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root,data)
height = myTree.getHeight(root)
print(height)

