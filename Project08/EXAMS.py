def is_perfect_square(number):
    # Calculate the square root and check if it's an integer
    sqrt_num = number**0.5
    if sqrt_num.is_integer():
        return "This number is a perfect square"
    else:
        return "This number is not a perfect square"


def calc_grades(D, college_name):
    for college_dict in D.values():
        if college_name in college_dict:
            grades = college_dict[college_name]
            return set(grades)
        return "College not found"


def average_grades(D, college_name):
    for college_dict in D.values():
        if college_name in college_dict:
            grades = college_dict[college_name]
            if grades == []:
                return None
            else:
                average_grades = sum(grades)/len(grades)
                return average_grades
        else:
            return None


class WizardCash:
    def __init__(self, sickles=0, knuts=0):
        # Initialize sickles and knuts only after validating them as non-negative integers
        sickles = sickles if isinstance(sickles, int) and sickles >= 0 else 0
        knuts = knuts if isinstance(knuts, int) and knuts >= 0 else 0

        # Convert total knuts into sickles and adjust the knuts value accordingly
        self.sickles = sickles + knuts // 29
        self.knuts = knuts % 29

    def __str__(self):
        return f"{self.sickles}:{self.knuts}"

    def __repr__(self):
        return str(self) #f"WizardCash(sickles={self.sickles}, knuts={self.knuts})"

    def __add__(self, other):
        if isinstance(other, WizardCash):
            return WizardCash(self.sickles + other.sickles, self.knuts + other.knuts)



# Example usage:
cash1 = WizardCash(10, 70)
print(cash1)  # Output: 12:12

cash2 = WizardCash(-10, 100)
print(cash2)  # Output: 3:11

result = cash1 + cash2
print(result)  # Output: 15:23