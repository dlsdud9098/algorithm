video_len, pos, op_start, op_end, commands, result = "34:33", "13:00", "00:55",	"02:55", ["next", "prev"], "13:00"
video_len, pos, op_start, op_end, commands, result = "10:55",	"00:05",	"00:15",	"06:55",	["prev", "next", "next"],	"06:55"
# video_len, pos, op_start, op_end, commands, result = "07:22",	"04:05",	"00:15",	"04:07",	["next"],	"04:17"

# 시간을 숫자로 바꿈
video_len = int(video_len.replace(':', ''))
pos = int(pos.replace(':', ''))
op_start = int(op_start.replace(':', ''))
op_end = int(op_end.replace(':', ''))

for com in commands:
    # 현재 pos가 op_start와 op_end 사이에 있을 때
    if (op_start <= pos) and (op_end >= pos):
        pos = op_end

    if com == 'next':
        pos += 10
        if pos >= video_len: 
            pos = video_len
            continue
        # pos의 초가 60을 넘어갈 때
        if (pos % 100 )> 59:
            pos -= 60   # 60초 빼기 
            pos += 100  # 1분 더하기 


    else:
        pos -= 10
        if pos <= 0:
            pos = 0
            continue

        if (pos % 100) > 59:
            pos -=40
    print(pos)
if (op_start <= pos) and (op_end >= pos):
    pos = op_end


pos = f'{pos // 100:02d}:{pos % 100:02d}'

print(result == pos)