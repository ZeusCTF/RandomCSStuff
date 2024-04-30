def main(image):
    mid = round(len(image[0]) / 2)
    
    for arr in image:
        count = -1
        for i in range(0, mid):
            last = arr[count]
            arr[count] = arr[i]
            arr[i] = last
            count -= 1
    print(image)

   
        


main([[1,1,0], [0,1,0]])
