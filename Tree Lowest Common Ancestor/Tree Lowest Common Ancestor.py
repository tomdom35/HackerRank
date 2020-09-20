

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    a1 = getAncestors(root, v1)
    a2 = getAncestors(root, v2)
    i = 0

    while i<len(a1) and i < len(a2) and a1[i] == a2[i]:
        i += 1

    return a1[i-1]

def getAncestors(root,v):
    curNode = root
    ancestors = [curNode]
    while(curNode != None and curNode.info != v):
        if v > curNode.info:
            curNode = curNode.right
        else:
            curNode = curNode.left
        ancestors.append(curNode)
    return ancestors


