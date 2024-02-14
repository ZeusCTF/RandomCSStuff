def main(arr):
    arr.sort()
    min_dif = arr[1] - arr[0]
    ans = []
 
    while arr:
        print(arr)
        new_arr = []
        if arr[1] - arr[0] == min_dif:
            new_arr.append(arr[0])
            new_arr.append(arr[1])
            ans.append(new_arr)
        arr.pop(1)
        arr.pop(0)
    print(ans)

        

main([1,3,6,10,15,20])