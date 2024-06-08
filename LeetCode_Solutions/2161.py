def main(nums, pivot):
    res = []
    nums.sort()
    #print(nums)
    for num in nums:
        if num < pivot:
            res.insert(0, num)
        elif num == pivot:
            res.append(num)
        else:
            res.append(num)
    print(res)

main([-3,4,3,2], 2)