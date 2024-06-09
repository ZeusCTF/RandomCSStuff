def main(nums, pivot):
    res = [pivot]
    count = 0

    for num in nums:
        if num < pivot:
            res.insert(count, num)
            count += 1
        elif num > pivot:
            res.append(num)
        else:
            res.insert((res.index(pivot) + 1), num)
    res.remove(pivot)
    print(res)

main([9,12,5,10,14,3,10], 10)

#quick note, I am VERY surpised this did not time out LMAO