"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

def solution(strs):
    count = 0
    ans = ''
    s = sorted(strs)
    print(s)
    for char in s[0]:
        
        if char == s[-1][count]:
            ans += char
        else:
            print(ans)
            return ans
        count += 1
   