import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['Bonus'] = employees['Salary'] * 0.1
    return employees
