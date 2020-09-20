# Enter your code here. Read input from STDIN. Print output to STDOUT

def heap(queries):
    h = [None]
    for q in queries:
        o = q[0]
        if o == 1:
            h.append(q[1])
            i = len(h) - 1
            while i > 1 and h[i] < h[int(i/2)]:
                t = h[int(i/2)]
                h[int(i/2)] = h[i]
                h[i] = t
                i = int(i/2)
        elif o == 2:
            i = h.index(q[1])
            l = len(h) - 1
            if i == l:
                h.pop()
            else:
                h[i] = h[l]
                h.pop()
                lc = i*2
                rc = (i*2)+1
                while (lc < len(h) and h[lc] < h[i]) or (rc < len(h) and h[rc] < h[i]):
                    if lc < len(h) and h[lc] < h[i] and rc < len(h) and h[rc] < h[i]:
                        if h[lc] < h[rc]:
                            new_i = lc
                        else:
                            new_i = rc
                    elif lc < len(h) and h[lc] < h[i]:
                        new_i = lc
                    elif rc < len(h) and h[rc] < h[i]:
                        new_i = rc
                    t = h[new_i]
                    h[new_i] = h[i]
                    h[i] = t
                    i = new_i
                    lc = i*2
                    rc = (i*2)+1
        else:
            print(h[1])
        

num_queries = int(input())
queries = []
for i in range(num_queries):
    queries.append(list(map(int, input().split())))

heap(queries)
