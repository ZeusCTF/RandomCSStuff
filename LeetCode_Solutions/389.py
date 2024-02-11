def main(s,t):
    s_val = 0
    t_val = 0
    for letter in s:
        s_val += ord(letter)
    for letter in t:
        t_val += ord(letter)
    if len(s) > len(t):
        print(s_val - t_val)
        print(chr(s_val - t_val))

main("helloy", "hello")