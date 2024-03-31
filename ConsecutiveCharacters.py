class Solution:
    def maxPower(self, s: str) -> int:
        max_con = 1
        temp = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                temp += 1
            else:
                temp = 1

            max_con = max(max_con, temp)

        return max_con

    # I set max_con to 1 and temp to 1
    # Iterate through the string starting at index 1, so I can compare the current character to the previous character,
    # so I don't have to move the pointer one step constantly if I were to start at index 0 and move forward
    # If the current character is equal to the previous character
    # Increment temp by 1
    # Else set temp to 1
    # Set max_con to the max of max_con and temp
    # Return max_con
