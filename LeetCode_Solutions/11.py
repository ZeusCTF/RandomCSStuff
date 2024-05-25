def main(height):
    x = 0
    y = len(height) - 1
    water = 0

    if len(height) == 2:
        return min(height) * 2

    while y >= x:   
        area = min(height[x], height[y]) * (y - x)
        if area > water:
            water = area
        else:
            if height[x] > height[y]:
                y -= 1
            else:
                x += 1
                
main([2,3,4,5,18,17,6])

