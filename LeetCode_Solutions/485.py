def main(inp):

    count = 0
    max_count = 0

    for num in inp:
        if num == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
            
    print(max_count)

        

main([1,1,0,1,1,1])