def distance(currentN,nextN):
    keypad = {1:(0,0), 2:(1,0), 3:(2,0),
              4:(0,1), 5:(1,1), 6:(2,1),
              7:(0,2), 8:(1,2), 9:(2,2),
              '*':(0,3), 9:(1,3), '#':(2,3)}
    
    x1,y1 = keypad[currentN]
    x2,y2 = keypad[nextN]
    
    return abs(x1-x2)+abs(y1-y2)

def solution(numbers, hand):
    answer = ''
    current_L='*'
    current_R='#'
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            current_L = i
        elif i in [3,6,9]:
            answer += 'R'
            current_R = i
        elif i in [2,5,8,0]:
            if distance(current_L,i) > distance(current_R,i):
                answer += 'R'
                current_R = i
            elif distance(current_L,i) < distance(current_R,i):
                answer += 'L'
                current_L = i
            else:
                if hand=='left':
                    answer +='L'
                    current_L = i
                else:
                    answer += 'R'
                    current_R = i
    return answer
