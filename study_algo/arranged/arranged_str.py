s = list(input())
s.sort()

answer = ''
answer2 = ''

for i in s:
    if i.isalpha():
        answer+= i
    else:
        answer2+= i

print(answer+answer2)