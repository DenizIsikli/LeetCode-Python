class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            temp = self.countAndSay(n-1)
            count = 1
            result = ""

            for i in range(1, len(temp)):
                if temp[i] == temp[i-1]:
                    count += 1
                else:
                    result += str(count) + str(temp[i-1])
                    count = 1

            result += str(count) + temp[-1]
            return result

    # Firstly I check if n is 1, if so, I return "1".
    # Otherwise, I recursively call the function with n-1, meaning I get the result of the previous number because
    # the sequence is based on the previous number.
    # I initialize count to 1 and result to an empty string.
    # I iterate through the range of 1 to the length of the previous result.
    # If the current character is equal to the previous character, I increment the count.
    # Otherwise, I add the count and the previous character to the result and reset the count to 1.
    # I add the count and the last character to the result.
    # Finally, I return the result.
