def main(image):

    mid = round(len(image[0]) / 2)

    
    
    for arr in image:
        count = -1
        for i in range(0, mid):

            last = arr[count]
            first = arr[i]

            if last == 1:
                last = 0
            else:
                last = 1
            
            if first == 1:
                first = 0
            else:
                first = 1
            
            arr[count] = first
            arr[i] = last
            count -= 1

    print(image)