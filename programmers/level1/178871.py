def solution(players, callings):
    answer = []
    # 순위별 선수 이름
    rank_player = {
        rank: player for rank, player in enumerate(players)
    }
    
    # 선수의 현재 순위
    player_rank = {
        player: rank for rank, player in enumerate(players)
    }
    
    
    for call in callings:
        # 이름이 불린 선수의 순위
        now_call_player_rank = player_rank[call]
        # 이름이 불린 선수의 앞 순위 선수 이름
        prev_player = rank_player[now_call_player_rank - 1]
        # 이름이 불런 선수의 앞 선수 순위
        prev_player_rank = player_rank[prev_player]
        
        # 이름이 불린 선수의 순위를 -1
        player_rank[call] -= 1
        # 앞 순위의 선수 순위 + 1
        player_rank[prev_player] += 1
        
        
        # 순위별 선수 이름에서 현재 이름이 불린 선수의 순위와 그 앞 선수의 위치(순위)를 바꿈
        rank_player[now_call_player_rank], rank_player[prev_player_rank] = rank_player[prev_player_rank], rank_player[now_call_player_rank]
        
    
    # 순위별로 선수를 삽입
    for rank, player in rank_player.items():
        answer.insert(rank, player)
        
    return answer
