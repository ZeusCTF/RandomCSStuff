def countPairs(nums, k):
    count = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                if (i * j) % k == 0:
                    count += 1
                    
    print(count)
        


countPairs([3,1,2,2,2,1,3], 2)