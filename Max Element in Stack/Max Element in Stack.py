# Enter your code here. Read input from STDIN. Print output to STDOUT

def stack(queries):
    stack = []
    track = []
    for q in queries:
        if q[0] == 1:
            stack.insert(0,q[1])
            if len(track) == 0:
                track.insert(0,q[1])
            elif q[1] > track[0]:
                track.insert(0,q[1])
            else:
                track.insert(0,track[0])
        elif q[0] == 2:
            stack.pop(0)
            track.pop(0)
        else:
            print(track[0])

num_queries = int(input())
queries = []
for i in range(num_queries):
    queries.append(list(map(int, input().split())))

stack(queries)
