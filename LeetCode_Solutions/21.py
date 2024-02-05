# https://www.geeksforgeeks.org/singly-linked-list-definition-meaning-dsa/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def main():
    head = curr = ListNode()  # The base of our chai

    while list1 and list2:  # As we brew, we choose the best leaf or spice
        if list1.val < list2.val:  # Adding l1 into the mix
            curr.next = list1
            list1 = list1.next
        else: 
            curr.next = list2
            list2 = list2.next
        
        curr = curr.next
    
    curr.next = list1 if list1 else list2

    return head.next