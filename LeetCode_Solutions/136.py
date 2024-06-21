def main(nums):
    x = 2
    for num in nums:
        if num ^ x == 0:
            pass
        else:
            x = num
    print(x)
        

main([4,1,2,1,2])