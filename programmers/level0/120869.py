def solution(spell, dic):
    # 경우의 수 모듈
    import itertools
    answer = 0
    spell_list = []
    
    # 경우의 수 뽑고 저장하기
    con = list(itertools.permutations(spell,len(spell)))
    for j in con:
        spell_list.append(''.join(j))
    
    # 있는지 확인하기
    for i in spell_list:
        if i in dic:
            answer = 1
            break
        else:
            answer = 2
    return answer