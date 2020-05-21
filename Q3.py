# Import json module
import json


def get_top_class(number):
    """
    Calculating student score average marks and select the top three classes
    :return: name of the top three classes
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
        # Creating an empty list to store student student average marks of each class
        student_avg_marks = []
        # iterate as the length of the class length
        for i in range(len(classes)):
            count = 0
            marks = 0
            # Getting each student detail from the report
            for student in report:
                # Check whether the class name equals with student class name
                if student['class'] == classes[i]:
                    marks += int(student['literature']) + int(student['math']) + student['science'] + student['english']
                    count += 1
                else:
                    pass
            # Append the calculated average scores of each class
            student_avg_marks.append(round((marks / (4 * count)), 2))

        # Use of higher order function to zip two lists
        overall_class_avg = list(zip(classes, student_avg_marks))
        print("These are the average student scores at each class\n ------------------------------------ ")
        print(overall_class_avg)

        # Sorting the student average marks and get the highest 3 average marks
        stu_avg_marks_sort = sorted(list(set(student_avg_marks)))[-number:]

        # Defining empty list to store top 3 classes
        top_classes = []

        position = 2
        # Calling for loop to identify the top 3 classes
        for x in range(len(stu_avg_marks_sort)):
            for y, z in overall_class_avg:
                if stu_avg_marks_sort[position] == z:
                    top_classes.append(y)
                else:
                    pass
            position = position - 1
        # Returning top 3 classes
        return top_classes

    except Exception as e:
        print(e)


if __name__ == '__main__':

    top_3_classes = get_top_class(3)
    print("The top three classes of grade 10 are: ", top_3_classes)

