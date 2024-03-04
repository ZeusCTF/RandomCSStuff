def main(nums):
    x = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[x] = nums[i]
            x += 1
    print(nums)
    print(x)


main([1,1,2])