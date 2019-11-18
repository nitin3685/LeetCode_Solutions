# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        result_ptr = result
        l1_ptr = l1
        l2_ptr = l2
        carry_over = 0
        while True:
            sum_val = 0
            if l1_ptr != None and l2_ptr != None:
                sum_val = l1_ptr.val + l2_ptr.val + carry_over
                l1_ptr = l1_ptr.next
                l2_ptr = l2_ptr.next
                result_ptr.val = sum_val % 10 
                carry_over = sum_val // 10
            elif l1_ptr != None:
                sum_val = l1_ptr.val + carry_over
                l1_ptr = l1_ptr.next
                result_ptr.val = sum_val % 10
                carry_over = sum_val // 10
            elif l2_ptr != None:
                sum_val = l2_ptr.val + carry_over
                l2_ptr = l2_ptr.next
                result_ptr.val = sum_val % 10
                carry_over = sum_val // 10
            else:
                result_ptr.val+=carry_over
                carry_over = 0
            if l1_ptr == None and l2_ptr == None and carry_over == 0:
                break
            result_ptr.next = ListNode(0)
            result_ptr = result_ptr.next

            
        return result   
