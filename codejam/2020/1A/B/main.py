def calcPath(n):
    path = []
    if n<=6:
        for i in range(1, n+1):
            path.append([i,i])
    elif n <= 501 and n>6:
        count=n
        path = [[1,1],[2,2],[2,1],[3,2],[3,3]]
        count-=6
        for i in range(count):
            path.append([4+i, 4+i])
    elif n <= 10000:
        path = [[1,1]]
        sum = 1
        row = 2
        while sum < n:
            sum += (row-1)
            if sum <= n:
                path.append([row, 2])
                row+=1
        if sum != n:
            sum-= (row-1)
        if sum<n:
            row-=1
            for j in range(n-sum):
                path.append([row, 1])
                row+=1
    """
    else:
        path = [[1,1],[2,2],[3,3]]
        sum = 3
        row = 3
        last = 1
        while (sum+(row-1)) < n:
            currentVal = last + row-1
            sum+= currentVal
            last = currentVal
            if (sum+(row-1)) <= n:
                path.append([row, 3])
                row+=1
            if sum != n:
                sum -= last
            if sum < n:
                path.append([row, 2])
                row-=1
                for j in rang(n-sum):
                    path.append([row, 1])
                    row+=1
    """
    return path

def printPath(path, case):
    print("Case #" + str(case) + ":")
    for part in path:
        myStr = ""
        myStr+= str(part[0]) + " "
        myStr+= str(part[1])
        print(myStr)

if __name__ == "__main__":
    t = int(input())
    for k in range(t):
        n = int(input())
        printPath(calcPath(n), k+1)
