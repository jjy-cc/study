n = input()

count1, count2 = 0, 0

if n[0] == '1':
    count1 += 1
else:
    count2 += 1

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        if n[i+1] == '1':
            count1+=1
        else:
            count2+=1

print(min(count1, count2))