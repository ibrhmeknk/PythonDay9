student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}
for student in student_scores:
    if student_scores[student] > 91:
        student_scores[student] = "Outstanding"
    elif 90 > student_scores[student] > 80:
        student_scores[student] = "Exceeds Expectations."
    elif 80 > student_scores[student] > 71:
        student_scores[student] = "Acceptable"
    elif 70 > student_scores[student]:
        student_scores[student] = "Fail."
    print(f"Students name: {student}, score: {student_scores[student]}")