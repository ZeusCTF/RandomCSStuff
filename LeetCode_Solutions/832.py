def main(image):
    if len(image[0]) > 1:
        mid = round(len(image[0]) / 2)

        
        
        for arr in image:
            for i in range(0, mid):

                last = arr[~i]
                first = arr[i]           
                arr[~i] = abs(first - 1)
                arr[i] = abs(last - 1)

        print(image)
    else:
        print([[abs(image[0][0] - 1)]])
    
main([[1,1,0],[1,0,1],[0,0,0]])
