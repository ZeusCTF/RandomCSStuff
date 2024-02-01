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
        elif len(stack) > 0 and x == bracket[stack[-1]]:
            stack.pop()
        else:
            return False
    return not stack