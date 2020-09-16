
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root == None: return 0
    
    lHeight = 0
    rHeight = 0
    if(root.left != None):
        lHeight = height(root.left) + 1
    if(root.right != None):
        rHeight = height(root.right) + 1
        
    if(lHeight > rHeight):
        return lHeight
    elif(rHeight > lHeight):
        return rHeight
    else:
        return 0

