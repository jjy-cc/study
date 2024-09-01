def solution(order):
    answer = 0
    container = []
    item = 1
    target = 0
    while True:
        # 물건이 배송순서가 아닐경우
        #if item in container or item > len(order) - 1 or target > len(order) - 1:
        if item in container or item > len(order)+1 or target >= len(order):
            break

        while container and container[-1] == order[target]:
            # 컨테이너 마지막이 배송 순서일경우
            container.pop()
            answer += 1
            target += 1
            print(container)

        container.append(item)
        item += 1
        print(container, item)
    return answer

#a = [4, 3, 1, 2, 5]
a = [5, 4, 3, 2, 1]
b = solution(a)

print(b)