def main(arr):
    count = 0

    for num in arr:
        if num % 2 != 0:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

        

print(main([1,2,34,3,4,5,7,23,12]))