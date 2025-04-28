wallpaper, result = [".#...", "..#..", "...#."],	[0, 1, 3, 4]
# wallpaper, result = ["..........", ".....#....", "......##..", "...##.....", "....#....."],	[1, 3, 5, 8]
# wallpaper, result = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."],	[0, 0, 7, 9]
# wallpaper, result = ["..", "#."],	[1, 0, 2, 1]

wallpaper_map = {}

for i, wall in enumerate(wallpaper):
    for j, n in enumerate(wall):
        wallpaper_map[f'{str(i)}, {str(j)}'] = n
        # print(n)
        
