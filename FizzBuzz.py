class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                answer.append("FizzBuzz")
            elif i%3==0:
                answer.append("Fizz")
            elif i%5==0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

    # I create a list to the answers, where I then iterate through "n"
    # and if "i" is divisible by 3 and 5, I append "FizzBuzz" to the created list.

    # If it's divisible by 3 only, I append "Fizz" to the created list.

    # If it's divisible by 5 only, I append "Buzz" to the created list.

    # Lastly I return the list