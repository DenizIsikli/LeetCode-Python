# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = output = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                output.next = list1
                list1 = list1.next
            else:
                output.next = list2
                list2 = list2.next
            output = output.next

        if list1: output.next = list1
        if list2: output.next = list2

        return dummy.next

    # I firstly create a node called "dummy" and "output" from the given class
    # where I check if both lists exists.

    # I then check if the value of the first list is lower than the value of the second list

    # If it is, I then assign the next position of the "output" node to the first list since you want the lower value
    # first (sorted), and I then go one further position in the first list since I've just used the previous element

    # Vice versa I check whether the second lists value is smaller than the first lists value

    # If it is, I then assign the next position of the "output" node to the second list since you want the lower value
    # first (sorted), and I then go one further position in the second list since I've just used the previous element

    # At the end of the while loop, I go one position further in "output"

    # I then check if there are still elements left in both lists, and if there is
    # I assign the next positions value of "output" to both the first list and second list

    # At last, I return "dummy.next"