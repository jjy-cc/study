n, m = map(int, input.split())
data = list(map(int, input.split()))

array = [0] * (m+1)

for x in data:
    array[x] += 1 #각 무게에 해당하는 볼링공의 개수 카운트
    
result = 0

for i in range(1, m+1):
    n -= array[i] #무게가 i인 볼링공의 개수 제외
    result += array[i] # B가 선택하는 경우의 수와 곱하기