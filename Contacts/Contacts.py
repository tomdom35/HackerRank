#!/bin/python3

import os
import sys

class Node:
  def __init__(self, data, children, endNode, count):
    self.data = data
    self.children = children
    self.endNode = endNode
    self.count = count

#
# Complete the contacts function below.
#
def contacts(queries):
    root = Node('',[],False,0)
    nums = []
    for q in queries:
        if(q[0] == "add"):
            addWord(q[1],root)
        else:
            n = wordCount(q[1],root)
            nums.append(n)
    return nums

def addWord(word, root):
    curNode = root
    done = False
    for c in word:
        contains = False
        if not done:
            for child in curNode.children:
                if child.data == c:
                    contains = True
                    newNode = child
                    newNode.count+=1
                    break
        if (not contains) or done:
            done = True
            end = c == word[len(word)-1]
            newNode = Node(c,[],end,1)
            curNode.children.append(newNode)
        curNode = newNode

def wordCount(partial, root):
    curNode = root
    for c in partial:
        found = False
        if curNode.children == []:
            #print('test1'+c+str(0))
            return 0
        for child in curNode.children:
            if child.data == c:
                curNode = child
                found = True
                break
        if not found:
            #print('test2'+c+str(0))
            return 0
    #print('test3' + curNode.data + str(curNode.count))
    return curNode.count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
