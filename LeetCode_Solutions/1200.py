def main(arr):
    arr.sort()
    min_dif = abs(arr[1] - arr[0])
    ans = []
    i = 0
    j = 1

    while j < len(arr):
        new_arr = []
        if abs(arr[j] - arr[i]) == min_dif:
            new_arr.append(arr[i])
            new_arr.append(arr[j])
            ans.append(new_arr)
        print(i)
        print(j)
        print()
        i += 1
        j += 1
    print(ans)
    
        

        

main([1,3,6,10,15])