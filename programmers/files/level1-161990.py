wallpaper, result = [".#...", "..#..", "...#."],	[0, 1, 3, 4]
# wallpaper, result = ["..........", ".....#....", "......##..", "...##.....", "....#....."],	[1, 3, 5, 8]
# wallpaper, result = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."],	[0, 0, 7, 9]
# wallpaper, result = ["..", "#."],	[1, 0, 2, 1]

wallpaper_map = {}

file_num = 0
for i, wall in enumerate(wallpaper):
    for j, n in enumerate(wall):
        wallpaper_map[f'{str(i)}, {str(j)}'] = n
        if n == '#':
            file_num += 1

drag = []
for key, value in wallpaper_map.items():
    for key, value in wallpaper_map.items():
        pass
    
print(file_num)