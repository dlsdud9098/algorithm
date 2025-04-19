import random

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine", "kai"]

# 선수 이름 리스트 생성 (영문 이름, 최대 6글자)
# players = [f"Player{i:04}" for i in range(1, 1001)]  # Player001, Player002, ..., Player100

# calling 리스트 생성 (임의로 이름을 50번 호출)
random.seed(42)  # 재현 가능성을 위한 랜덤 시드 설정
# callings = [random.choice(players) for _ in range(500)]

answer = []
player_rank = {}
for rank, player in enumerate(players):
    player_rank[player] = rank

# player_rank_list = list(player_rank.items())

for call in callings:
    up_player = player_rank[call]
    player_rank[call] -= 1
    value = player_rank[call]

    down_player = list(player_rank.items())[value][0]
    player_rank[down_player] += 1

for player, rank in player_rank.items():
    answer.insert(rank, player)

print(answer)