def main(x):
    lower = 0
    upper = x

    while lower <= upper:
        test = (upper + lower) // 2
        test_squared = test * test

        if test_squared > x:
            upper = test
        elif test_squared < x:
            lower = test
        else:
            return test


main(100)

"""
I ended up looking at a solution for this, and this is what the solution was:

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
            
        return right

I am not really sure why my code does not return an answer quickly enough, despite almost the exact same implementation.  I did try adding the second return, however that did not work either.
I will note, the test cases were 4 and 8.  So there really isn't any reason for my code to time out, like there could be if the integer was something around 912312394952349871325
"""
