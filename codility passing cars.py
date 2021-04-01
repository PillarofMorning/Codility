

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    arr = 0
    passed = 0
    for x in A:
        if passed >= 1000000000:
            return -1
        if x == 0:
            arr+=1
        if x == 1:
            passed += arr
    return passed



print(solution( [1, 2, 1]))