n = int(input())
data = list(map(int, input().split()))

def binary_search(start, end, array):
    if start >= end:
        return -1

    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(start, mid-1, array)
    else:
        return binary_search(mid+1, end, array)

answer = binary_search(0, len(data)-1, data)
print(answer)