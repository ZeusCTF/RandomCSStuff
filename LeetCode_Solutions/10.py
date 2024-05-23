def main(height):
    max = 0
    x = 0
    y = -1
    size = len(height)



    def volume(x, y, distance):
        total = x * y * distance

        print(f"x: {x} y: {y}")
        print(f"distance: {distance}")
        print(f"total: {total}")
        return total
    
    while x != y:
        fstep = height[x]
        lstep = height[y]
        run = volume(fstep, lstep, (size - x))
        if run < max:
            print(max)
            return max
        else:
            x += 1
            y -= 1
            print(f"x: {x} y: {y}")
            max = run




main([1,8,6,2,5,4,8,3,7])