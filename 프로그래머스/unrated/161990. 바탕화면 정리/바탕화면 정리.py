def solution(wallpaper):
    xu = 0
    xd = len(wallpaper[0])
    yu = 0
    yd = len(wallpaper)
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == "#":
                yd = min(y,yd)
                yu = max(y,yu)
                xd = min(x,xd)
                xu = max(x,xu)
        
    return yd,xd,yu+1,xu+1