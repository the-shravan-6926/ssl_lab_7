
def calculate_grade(marks):
    if isinstance(marks, bool) or not isinstance(marks, (int, float)):
        raise TypeError("Marks must be a number")

    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    if marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"
