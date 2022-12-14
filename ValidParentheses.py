class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {")": "(", "]": "[", "}": "{"}

        for p in s:
            if p in dict:
                if stack and stack[-1] == dict[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return stack == []