class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            current.next, prev, current = prev, current, current.next  
            
        return prev
