def main(nums):
    nums = sorted(nums)
    for num in nums:
        if nums[nums.index(num) + 1] == num:
            print('dup')
            break

main([1,2,2,4])