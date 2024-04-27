def main(image):
    for arr in image:
        arr.reverse()
        for ele in arr:
            if ele == 1:
               arr[ele] = 0
               
        print(arr)
    print(image)




    """
        for i in arr:
            if arr[i] == 1:
                arr[i] = 0
            elif arr[i] == 0:
                arr[i] = 1
    """
   
        


main([[1,1,0], [0,1,0]])
