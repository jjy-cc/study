n = int(input())
data = []
for _ in range(n):
    name, grade = input().split()
    data.append([name, int(grade)])

data.sort(key=lambda x : x[1])
print(data)