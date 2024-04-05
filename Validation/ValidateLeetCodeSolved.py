import os


class ValidateLeetcodeSolved:
    def __init__(self):
        self.leetcode_dir = os.path.dirname("../LeetCode")

    def validate(self) -> int:
        count = 0
        for file in os.listdir(self.leetcode_dir):
            if file.endswith(".py"):
                count += 1
        return count


if __name__ == "__main__":
    vls = ValidateLeetcodeSolved()
    print(vls.validate())
