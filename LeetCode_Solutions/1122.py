def main(arr1, arr2):
    result = []
    
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr1[j] == arr2[i]:
                result.append(arr1[j])
                arr1[j] = -1
    
    arr1.sort()
    
    for num in arr1:
        if num != -1:
            result.append(num)
            
    return result


   


main([28,6,22,8,44,17], [22,28,8,6])
