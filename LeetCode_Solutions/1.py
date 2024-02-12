"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
"""
https://www.geeksforgeeks.org/python-itertools-combinations-function/#
https://docs.python.org/3/library/itertools.html
"""

def main(nums, target):
    import itertools
    pair = []
    indexes = []
    for (ix, x), (iy, y) in itertools.combinations(enumerate(nums),2):
        if x + y == target:
            pair.append((x, y))
            indexes += (ix, iy)
    print(indexes)

