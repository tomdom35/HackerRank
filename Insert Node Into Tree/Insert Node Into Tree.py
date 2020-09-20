

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        newNode = Node(val)
        if self.root == None:
            self.root = newNode
            return self
            
        curNode = self.root
        inserted = False

        while not inserted:
            if val < curNode.info:
                if curNode.left == None:
                    curNode.left = newNode
                    inserted = True
                else:
                    curNode = curNode.left         
            if val > curNode.info:
                if curNode.right == None:
                    curNode.right = newNode
                    inserted = True
                else:
                    curNode = curNode.right

        return self.root


