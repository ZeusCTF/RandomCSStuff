def main(s,t):
    s_val = 0
    t_val = 0
    for letter in s:
        s_val += ord(letter)
    for letter in t:
        t_val += ord(letter)
    return chr(t_val - s_val)

main("helloy", "hello")