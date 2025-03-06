def solution(quiz):
    o_x = []
    for i in range(len(quiz)):
        now_quiz = quiz[i]
        equal_num = now_quiz.find('=')
        calc = now_quiz[:equal_num]
        answer = now_quiz[equal_num+1:].replace(' ','')
        
        if ' - ' in calc:
            sub = calc.find(' - ')
            result = int(calc[:sub]) - int(calc[sub+2:])
        elif ' + ' in calc:
            sub = calc.find(' + ')
            result = int(calc[:sub]) + int(calc[sub+2:])
        
        if int(result) == int(answer):
            o_x.append('O')
        else:
            o_x.append('X')
            
    return o_x
        