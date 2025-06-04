number = int(input())

answer = 0

# 반복하는 횟수를 자리수 / 2 값의 몫으로 하면 된다.
# 4자리수 -> 2번, 6자리수 -> 3번...
for i in range(len(str(number)) // 2):
    answer += number % 100
    number //= 100

print(answer)