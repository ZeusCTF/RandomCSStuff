def main(timeSeries, duration):
    l = len(timeSeries)
    total = 0

    for i in range(l):
       if i < l - 1:
           if timeSeries[i + 1] - timeSeries[i] >= duration:
               total += duration
           else:
               total += timeSeries[i + 1] - timeSeries[i]

       else:
           total += duration
    
    print(total)

        
main([1,4],2)