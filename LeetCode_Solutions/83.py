class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def main(head):
    current = head

    while current:
        while current.next and current.next.val == current.val:
            current.next = current.next.next
        current = current.next
    return head

                