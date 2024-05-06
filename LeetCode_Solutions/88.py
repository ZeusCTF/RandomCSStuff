def main(nums1, m, nums2, n):
    for i in range(0,n):
        nums1[m] = nums2[i]
        m += 1
    print(sorted(nums1))
main([1,2,3,0,0,0], 3, [2,5,6], 3)