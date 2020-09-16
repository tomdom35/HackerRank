"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    l1 = [root]

    while(len(l1)>0):
        l2 = []
        for l in l1:
            print(l.info, end=" ")
            if(l.left != None):
                l2.append(l.left)
            if(l.right != None):
                l2.append(l.right)
        l1 = l2