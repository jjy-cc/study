n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse = True)

for i in range(k):
     a, b = min(arr1), max(arr2)
     if a > b:
         break
     else:
        arr1[i], arr2[i] = arr2[i], arr1[i]

print(sum(arr1))