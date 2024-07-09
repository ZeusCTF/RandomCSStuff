def main(nums):
    res = []

    nums = sorted(nums)
    for num in nums:
        if nums[nums.index(num) + 1] == num:
            res.append(num)
            res.append(num + 1)
            return res

print(main([1,2,2,4]))