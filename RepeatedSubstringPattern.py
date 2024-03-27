class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        index = 0
        incr = 1

        substring = s[index:index + incr]

        while incr <= len(s) - incr:
            if substring * (len(s) // len(substring)) == s:
                return True

            incr += 1
            substring = s[index:index + incr]

        return False

    # I initialize the index and increment variables to 0 and 1, respectively.
    # I initialize the substring variable to the first character of the string.
    # I use a while loop to iterate through the string.
    # I check if the substring repeated len(s) // len(substring) times is equal to the string.
    # If it is, I return True.
    # If not, I increment the increment variable and update the substring variable.
    # If the loop completes without finding a repeated substring, I return False.
