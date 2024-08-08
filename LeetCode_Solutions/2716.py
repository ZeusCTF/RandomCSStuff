class Solution:
    def minimizedStringLength(self, s: str) -> int:
        res = ''
        for char in s:
            if char in res:
                pass
            else:
                res += char
        return len(res)
