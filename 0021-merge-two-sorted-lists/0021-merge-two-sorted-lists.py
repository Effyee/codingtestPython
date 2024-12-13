# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        c_node = answer
        
        while list1 and list2:
            if list1.val <= list2.val:
                c_node.next = list1
                list1 = list1.next
            else:
                c_node.next = list2
                list2 = list2.next
            c_node = c_node.next
        
        if list1:
            c_node.next = list1
        if list2:
            c_node.next = list2
        
        return answer.next
        