def main(nums):
    x = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[x] = nums[i]
            x += 1
    return nums
    return x


main([0,0,1,1,1,2,2,3,3,4])