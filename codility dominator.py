

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if A:
        z= sorted(A)
        dom = z[len(A)//2]
        x = A.count(dom)
        if x > len(A)//2:
            return A.index(dom)
        else:
            return -1
    else:
        return -1




print(solution( [1, 2, 1]))