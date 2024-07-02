def main(nums1, nums2):
    res = []

    i = {}
    j = {}

    for num in nums1:
        if num in i:
            i[num] += 1
        else:
            i[num] = 1

    for num in nums2:
        if num in j:
            j[num] += 1
        else:
            j[num] = 1

    
    if len(i) > len(j):
        for val in j:
            if val in i:
                res.append(val)
    else:
        for val in i:
            if val in j:
                res.append(val)
            
        return res
print(main([4,5,9],[9,4,9,8,4]))