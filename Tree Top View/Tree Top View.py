

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    c = [root.info]
    c_cur = 0
    c_max = [0]
    c_min = [0]
    findMinMax(root,c,c_cur,c_min,c_max)

    min_val = c_min[0] + 1
    max_val = c_max[0]

    print(c[0], end = ' ')

    while min_val <= max_val:
        searchNewMin(root,c,0,min_val,0,[-1])
        print(c[0], end = ' ')
        min_val+=1

def searchNewMin(node,c,c_cur,c_min,cur_depth,min_depth):
    if node != None:
        if c_cur == c_min and (cur_depth < min_depth[0] or min_depth[0] == -1):
            c[0] = node.info
            min_depth[0] = cur_depth
        else:
            searchNewMin(node.right, c, c_cur+1, c_min, cur_depth+1, min_depth)
            searchNewMin(node.left, c, c_cur-1, c_min, cur_depth+1, min_depth)

def findMinMax(node,c,c_cur,c_min,c_max):
    if node != None:
        if c_cur <= c_min[0]:
            c_min[0] = c_cur
            c[0] = node.info
        if c_cur > c_max[0]:
            c_max[0] = c_cur
        findMinMax(node.right,c,c_cur+1,c_min,c_max)
        findMinMax(node.left,c,c_cur-1,c_min,c_max)

