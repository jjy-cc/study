'''
n, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

print(data[k - 1])
'''
from itertools import permutations

n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
for i in permutations(data, m):
    for j in list(i):
        print(j, end = ' ')
    print()