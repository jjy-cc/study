import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))


def quick(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick(arr, start, right - 1)
    quick(arr, right + 1, end)


quick(data, 0, len(data) - 1)

for i in range(n):
    print(data[i])