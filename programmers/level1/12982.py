def solution(d, budget):
    # 많은 부서를 넣으려면 작은 숫자가 많이 들어가면 됨
    arr = sorted(d) # 오름차순 정렬
    n = 1   # 뽑을 원소의 개수
    
    while True:
        found = False   # 찾았는지 여부
        for i in range(len(arr) - n + 1):   
            # n개 만큼 원소의 개수 뽑은 숫자의 합이 budget보다 작으면
            if sum(arr[i:i+n]) <= budget:   
                found = True
                break
        if not found:
            return n-1
        n += 1