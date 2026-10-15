
import csv
from grading import calculate_grade


def generate_report(filename="students.csv"):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print(f"{'Name':<15} {'Marks':<10} {'Grade':<10}")
        print("-" * 35)

        for row in reader:
            name = row["name"]
            marks = float(row["marks"])

            try:
                grade = calculate_grade(marks)
                print(f"{name:<15} {marks:<10g} {grade:<10}")
            except (ValueError, TypeError) as error:
                print(f"{name:<15} {marks:<10g} REJECTED: {error}")


if __name__ == "__main__":
    generate_report()
