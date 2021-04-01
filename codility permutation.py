

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    arr = [0]
    truthy = 0
    for x in A:
        if x-1 == arr[-1]:
            truthy = 1
        else:
            truthy = 0
            break

        arr.append(x)
    return truthy




print(solution( [1, 2, 1]))