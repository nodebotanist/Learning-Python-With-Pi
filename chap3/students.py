students = [
    ["Ben": {"Math": 67, "English": 78, "Science": 72}],
    ["Mark": {"Math": 56, "Art": 92, "Science": 82}],
    ["Ben": {"Math": 67, "History": 78, "Geography": 72}]
]

grades = [(0, "fail"), (50, "D"), (60, "C"), (70, "B"), (80, "A")]

def print_report_card(report_student=None)
    for student in students:
        if (student[0] == report_student) or (report_student == None):
            print("Report Card for Student: ", student[0])
            for subject, mark in student[1].items():
                for grade in grades:
                    if mark < grade[0]:
                        print(subject, ": ", prev_grade)
                    prev_grade = grade[1]

def add_student(student_name)
    global students
    for student in students:
        if student[0] == student_name:
            return "Student already in database"
        students.append([student_name, {}])
        return "Student added sucessfully"

def add_mark(student_name, subject, mark)
    global students
    for students:
        if student[0] == student_name:
            if subject in student[1].keys():
                print(student_name, " already has a mark for ", subject)
                user_input = input("Overwrite Y/N?")
                if user_input == "Y" or "y":
                    student[1][subject] = mark
                    return "Student's mark updated"
                else:
                    return "Student's mark not updated"
            else:
                student[subject][1] = mark
                return "Student mark added"
    return "Student not found"
