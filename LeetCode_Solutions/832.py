def main(image):
    for arr in image:
        arr.reverse()
        for i in arr:
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    print(image)
   
        


main([[1,1,0], [0,1,0]])
