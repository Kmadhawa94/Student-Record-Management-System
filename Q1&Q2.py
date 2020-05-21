# Import json module
import json


def get_classes_avg(subject, avg):
    """
    Calculating average marks of each subject in each class and find the classes above given average
    :return: name of classes above average
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

    try:
        # Creating an empty list to store science average marks of each class
        subject_avg_marks = []
        # iterate as the length of the class length
        for i in range(len(classes)):
            count = 0
            marks = 0
            # Getting each student detail from the report
            for student in report:
                # Check whether the class name equals with student class name
                if student['class'] == classes[i]:
                    # Add the marks of particular subject
                    marks += int(student[subject])
                    count += 1
                else:
                    pass
            # Append the calculated average subject marks of each class
            subject_avg_marks.append(round((marks / count), 2))

        # Use of higher order function to zip two lists
        stu_subject_marks = list(zip(classes, subject_avg_marks))
        above_avg_classes = []
        # Check the classes having required subject avg. marks greater than given average
        for i, j in stu_subject_marks:
            if j >= avg:
                above_avg_classes.append(i)
            else:
                pass

        print("There are ", len(above_avg_classes), " classes having above-average 70 for" + subject)
        # Return the class names above average
        return above_avg_classes

    except Exception as e:
        return e


if __name__ == '__main__':
    top_science_classes = get_classes_avg("science", 70)
    print(top_science_classes)

    print("-------------------------------------------------------------")

    top_literature_classes = get_classes_avg("literature", 70)
    print(top_literature_classes)