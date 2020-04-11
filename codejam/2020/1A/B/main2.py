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
