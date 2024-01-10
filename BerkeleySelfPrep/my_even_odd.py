def main(start, end):
    for num in range(start, (end +1)):
        output = "EVEN" if num % 2 == 0 else "ODD"
        print(f"{num} {output}")
main(1,10)