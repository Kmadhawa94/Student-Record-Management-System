# Import json module
import json


def section_top():
    """
    Calculating student average marks and select the top scorer among all classes
    :return: class and student id
    """
    try:
        # Opening JSON file
        score_cards = open('student_socre.json')

        # Returns JSON objects as a list of dictionaries
        report = json.load(score_cards)

    except FileNotFoundError:
        print("File not found")

    # Defining the available classes
    classes = ['10-A', '10-B', '10-C', '10-D', '10-E', '10-F', '10-G', '10-H', '10-I']
    # Creating an empty list to store student student average marks of each class

    student_id = []
    all_students = []
    top_students = []
    student_details = []

    # iterate as the length of the class length
    for i in range(len(classes)):
        count = 4
        student_avg_marks = []

        try:
            # Getting each student detail from the report
            for student in report:
                marks = 0

                # Check whether the class name equals with student class name
                if student['class'] == classes[i]:
                    marks += int(student['literature']) + int(student['math']) + student['science'] + student['english']

                    # Append the calculated average scores of each class
                    student_avg_marks.append(round((marks / count), 2))

                    # Append student's ID
                    student_details.append([student['class'], student['student_id'], round((marks / count), 2)])
                else:
                    pass
            # Getting the highest average score in a particular class

        except Exception as e1:
            print(e1)

        top_students.append(max(student_avg_marks))
    highest_marks = max(top_students)

    try:
        count = 0
        for s in student_details:
            if s[2] == highest_marks:
                count += 1
                print("Number of section 1st places: ", count)
                print(f"Section top is from Class: {s[0]} & student ID: {s[1]}")

            else:
                pass
    except Exception as e2:
        print(e2)


if __name__ == '__main__':

    section_top()