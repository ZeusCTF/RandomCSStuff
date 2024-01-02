"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

def solution(num):
    num = str(num)
    rev_str = num[::-1]
    if rev_str == num:
        return True
    return False
