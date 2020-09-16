#!/bin/python3

import os
import sys
sys.setrecursionlimit(1500)

class Node:
  def __init__(self, data, leftChild, rightChild):
    self.data = data
    self.leftChild = leftChild
    self.rightChild = rightChild

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    root = buildTree(indexes)
    mList = []
    for q in queries:
        orderedList = []
        traverseSwap(root,q,1,1)
        orderedTraversal(root, orderedList)
        mList.append(orderedList)

    return mList

def orderedTraversal(node, oList):
    if(node.leftChild != None):
        orderedTraversal(node.leftChild, oList)
    oList.append(node.data)
    if(node.rightChild != None):
        orderedTraversal(node.rightChild, oList)


def buildTree(indexes):
    root = Node(1,None,None)
    nodes = [root]
    iNode = 0
    for i in indexes:
        cNode = nodes[iNode]

        if i[0] != -1:
            lNode = Node(i[0],None,None)
            nodes.append(lNode)
            cNode.leftChild = lNode

        if i[1] != -1:
            rNode = Node(i[1],None,None)
            nodes.append(rNode)
            cNode.rightChild = rNode

        iNode+=1

    return root

def traverseSwap(node, startDepth, inc, curDepth):



    if(node != None):
        #print('node: ' + str(node.data))
        #print('curDepth: ' + str(curDepth))
        #print()
        if(curDepth == startDepth*inc):
            tNode = node.leftChild
            node.leftChild = node.rightChild
            node.rightChild = tNode
            inc+=1
        
        traverseSwap(node.leftChild, startDepth, inc, curDepth+1)
        traverseSwap(node.rightChild, startDepth, inc, curDepth+1)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
