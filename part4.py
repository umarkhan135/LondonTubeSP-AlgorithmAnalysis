def bsp_solution(L, m):
    copyL = L.copy()
    result = bsp_value(L, m)
    count = 0
    for i in range(len(L) - 1):
        if count == m:
            break
        if copyL[i + 1] - copyL[i] < result:
            copyL.pop(i + 1)
            count += 1
    
    return copyL

def bsp_value(L, m):
    n = len(L)
    if n <= m:
        return 0
    else:
        if m == 0:
            minDist = float('inf')
            for i in range(1, n):
                if L[i] - L[i - 1] < minDist:
                    minDist = L[i] - L[i - 1]
            return minDist
        else:
            firstIdx = 0
            secIdx = 0
            minDist = float('inf')
            for i in range(1, n):
                if L[i] - L[i - 1] < minDist:
                    minDist = L[i] - L[i - 1]
                    firstIdx = i - 1; secIdx = i
            
            return max(bsp_value(L[:firstIdx] + L[firstIdx+1 :], m - 1), bsp_value(L[:secIdx] + L[secIdx+1 :], m - 1))

L = [2, 15, 31, 46, 56, 98]
L2 = [2, 4, 6, 7, 10, 14]
print(bsp_solution(L, 2))
print(bsp_solution(L2, 2))
