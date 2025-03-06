def solution(a, b):
    # 약분 모듈
    from fractions import Fraction
    
    # 기약분수 만들기
    fra = Fraction(a, b)
    # 분모 추출
    den = fra.denominator
    
    # 2와 5로 최대한 나누기
    print('/2')
    while den % 2 == 0:
        print(den)
        if den % 2 == 0:
            den = den // 2
        else:
            break
    print(den)
    print('/5')
    while den % 5 == 0:
        print(den)
        if den % 5 == 0:
            den = den // 5
        else:
            break
    
    # 끝까지 나누고 나서 분모가 1이면 유한소수, 아니면 2 리턴
    if den == 1:
        return 1
    else:
        return 2