def strongPasswordCheckerII(self, password: str) -> bool:
    if len(password) < 8:
        return False
    
    upper = False
    special = False
    nums = False
    lower = False

    special_chars = '!@#$%^&*()-+'
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_chars = '1234567890'
    lower_chars = 'abcdefghijklmnopqrstuvwxyz'

    prev = ''

    for char in range(0, len(password)):
        if password[char] == prev:
            return False
        elif password[char] in special_chars:
            special = True
        elif password[char] in upper_chars:
            upper = True
        elif password[char] in num_chars:
            nums = True
        elif password[char] in lower_chars:
            lower = True
        prev = password[char]


    if special and upper and nums and lower:
        return True
    else:
        return False