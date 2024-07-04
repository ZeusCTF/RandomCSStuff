def main(nums):
    averages = []
    nums = sorted(nums)

    while nums:
        i, j = nums[0], nums[-1]
        average = (i + j) / 2
        averages.append(average)

        nums.pop(0)
        nums.pop()

    return min(averages)



print(main([7,8,3,4,15,13,4,1]))