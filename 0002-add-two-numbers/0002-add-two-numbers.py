class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2, i = 0, 0, 1
        while l1 or l2:
            if l1:
                num1 += l1.val * i
                l1 = l1.next
            if l2:
                num2 += l2.val * i
                l2 = l2.next
            i *= 10
        s = num1 + num2
    
        answer = ListNode(0)
        current = answer
        if s == 0:
            return answer
        
        while s > 0:
            current.next = ListNode(s % 10)
            current = current.next
            s //= 10
        
        return answer.next
