# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        forward_list = []
        backward_list = []

        current = head
        while current:
            forward_list.append(current.val)
            backward_list.insert(0, current.val)
            current = current.next
        return forward_list == backward_list

# Time & Space: O(n)
