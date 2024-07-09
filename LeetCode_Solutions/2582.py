def main(n, time):
   time %= 2 * (n - 1)
   return time + 1 if time <= n - 1 else n - (time - (n - 1))

print(main(4, 5))