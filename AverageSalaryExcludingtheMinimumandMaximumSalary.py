class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))

        return sum(salary) / len(salary)

    # Remove the minimum salary from the list
    # Remove the maximum salary from the list
    # Return the sum of the list divided by the length of the list
