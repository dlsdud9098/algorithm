def solution(s):
    answer = ''
    
    numbers = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight':8 ,
        'nine': 9
    }
    
    string = ''
    for word in s:
        if not word.isnumeric():
            string += word
            if string in numbers:
                answer += str(numbers[string])
                string = ''
        else:
            answer += word
        
    return int(answer)