def solution(s, skip, index):
    answer = ''
    #a = 97, z = 122
    data = [chr(i) for i in range(97, 123)]
    avail_alpha = [i for i in data if i not in skip]
    
    for st in s:
        idx = avail_alpha.index(st)
        idx = (idx + index) % len(avail_alpha)
            
        answer += avail_alpha[idx]
    return answer
