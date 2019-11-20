# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_ptr = l1
        l2_ptr = l2
        if not l1_ptr and not l2_ptr:
            return None
        elif not l1_ptr:
            return l2_ptr
        elif not l2_ptr:
            return l1_ptr
        else:
            pass
        result = ListNode(0)
        result_ptr = result
        while True:
            if l1_ptr and l2_ptr:
                if l1_ptr.val <= l2_ptr.val :
                    result_ptr.val =l1_ptr.val
                    l1_ptr = l1_ptr.next
                    
                else:
                    result_ptr.val =l2_ptr.val
                    l2_ptr = l2_ptr.next

                result_ptr.next = ListNode(0)
                result_prev = result_ptr
                result_ptr = result_ptr.next

                
            elif l1_ptr:
                    result_ptr.val =l1_ptr.val
                    result_ptr.next = ListNode(0)
                    result_prev = result_ptr
                    result_ptr = result_ptr.next
                    l1_ptr = l1_ptr.next
                    
            elif l2_ptr:
                    result_ptr.val =l2_ptr.val
                    result_ptr.next = ListNode(0)
                    result_prev = result_ptr
                    result_ptr = result_ptr.next
                    l2_ptr = l2_ptr.next

            else :
                result_prev.next = None
                break
        
        return result
