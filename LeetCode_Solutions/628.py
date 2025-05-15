def maximumProduct(nums):
    nums = sorted(nums)
    ans1 = 1
    ans2 = 1

    for num in nums[-3::]:
        ans1 *= num

    ans2 = nums[0] * nums[1] * nums[-1]

    return max(ans1, ans2)


maximumProduct([1,2,3])