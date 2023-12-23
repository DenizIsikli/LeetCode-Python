class Solution:
    def totalMoney(self, n: int) -> int:
        week = 7
        increment = 0
        each_week = 0
        money = 0

        for i in range(n):
            if i % week == 0:
                each_week += 1
                increment = each_week
            else:
                increment += 1
            money += increment

        return money

    # I use a for loop to iterate through the number of weeks,
    # if it's the first day of the week, I increment the variable each_week by 1
    # and set the increment to each_week.
    # I then increment the variable increment by 1 for each day, until it's the end of the week,
    # meaning: (i % week == 0), in which case I increment each_week by 1 and set the increment to each_week,
    # meaning a new week has started.
    # At last, I return the money incremented by the variable increment.
