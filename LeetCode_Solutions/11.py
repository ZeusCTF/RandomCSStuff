def main(height):
    mX = 0
    x = 0
    y = -1
    size = len(height)



    def volume(x, y, distance):
        total = (min(x, y) ** 2) * distance

        print(f"x: {x} y: {y}")
        print(f"distance: {distance}")
        print(f"total: {total}")
        print()
        return max(x, y) * max(x, y)
    
    while x != y:
        fstep = height[x]
        lstep = height[y]
        run = volume(fstep, lstep, (size - x))
        if run < mX:
            print(mX)
            return mX
        else:
            if height[x] > height[y]:
                y -= 1
            else:
                x += 1
            #print(f"x: {x} y: {y}")
            mX = run




main([1,8,6,2,5,4,8,3,7])

