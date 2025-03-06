def solution(numbers, k):
    answer = 0
    
    # 공을 가지고 있는 사람의 index
    ball = (k-1) * 2 
    
    # 배열의 크기를 넘어가면 나머지 ball의 나머지 값을 구한다.
    if ball > len(numbers):
        ball = ball % len(numbers)
            
    return numbers[ball]