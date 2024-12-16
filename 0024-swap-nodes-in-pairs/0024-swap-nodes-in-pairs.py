class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        
        for i in range(0, len(l)-1, 2):
            l[i], l[i+1] = l[i+1], l[i]
        
        answer = ListNode(0)
        current = answer
        for i in l:
            current.next = ListNode(i)
            current = current.next
        return answer.next
