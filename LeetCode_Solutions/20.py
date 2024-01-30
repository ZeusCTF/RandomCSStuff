def main(s):
    stack = []
    bracket = {
        '(':')',
        '{':'}',
        '[':']'
    }

    for x in s:
        if x in bracket:
            stack.append(x)
        
main('()[]{}')