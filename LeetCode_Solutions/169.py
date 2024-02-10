def main(nums):
    nums.sort()
    return nums[int(len(nums) / 2)]

main([3,3,4])