def scoring_system(grade):
    students_grades = []
    for g in grade:
        if g < 40:
            g = 0
        elif g >= 40:
            def grade_round(n, base=5):
                return base * round(n / base)
            if grade_round(g) > g:
                g = grade_round(g)
            elif grade_round(g) < g:
                g = g
        students_grades.append(g)

    return students_grades
actual_grades = [66,39,89]
print(("actual grades : " + str(actual_grades)))
rounded_grades = scoring_system(actual_grades)
print("final grades: " + str(rounded_grades))