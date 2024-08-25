def solution(ingredient):
    answer = 0
    burger = ''
    pack = '1231'
    
    for ingre in ingredient:
        burger += str(ingre)
        
        if burger[-4:] == pack:
            answer += 1
            burger = burger[:-4]
            
    return answer
