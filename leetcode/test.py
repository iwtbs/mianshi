def Find_Police( N , trust ):
    # write code here
    no_can = set()
    tr = set()
    times = dict()
    for i,j in trust:
        no_can.add(i)
        tr.add(j)
        if i not in times:
            times[i] = [j]
        else:
            times[i].append(j)
    people = set(range(1,N+1))
    can = list(people - no_can)
    if len(can) == 0:
        return -1
    for _,v in times.items():
        if len(v) == 1:
            return v[0]

print(Find_Police(2,[[1,2]]))