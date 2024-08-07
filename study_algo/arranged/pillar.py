def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            # 바닥위, 혹은 보의 한쪽 끝부분 위, 혹은 다른 기둥 위라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            # 한쪽 끝부분이 기둥 위, 혹은 양쪽 끝 부분이 다른 보와 동시에 연결이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        elif operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
    return sorted(answer)