
def calculate_grade(marks):
    if not 0 <= marks <= 100:
        raise ValueError("Invalid marks")

    if marks >= 85:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"
