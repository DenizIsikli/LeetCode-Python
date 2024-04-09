class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters and convert to lowercase
        s = ''.join([c for c in s if c.isalnum()])
        return s.lower() == s[::-1].lower()

    # Firstly, I remove all non-alphanumeric characters from the string
    # Then I check if the string is equal to its reverse in lowercase
