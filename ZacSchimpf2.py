"""
    Zac Schimpf
    CSCI 1620 001/851
    Professor Owora
    Week 02 - Lab 02
    29/01/2024
"""


def main():
    """
    Main logic structure that accepts students & scores, creates grade scale, and prints results
    :return: None
    """

    students = get_students()
    scores = get_scores(students)
    grade_scale = get_grade_scale(scores)
    output(scores, grade_scale)


def get_students():
    """
    Requests input of quantity of students
    :return: int value of students
    """

    students = input("Total number of students: ").strip()
    try:
        students = int(students)

        if students < 0:
            raise IndexError

    except IndexError:
        print("\"" + str(students) + "\" must be a positive whole-number integer value")
        students = get_students()

    except ValueError:
        print("\"" + str(students) + "\" must be a whole-number integer value, please try again.")
        students = get_students()

    return students


def get_scores(students):
    """
    Requests input of score and appends letter grade scale
    :param students: int quantity of students
    :return: List[] containing int scores; e.g. [100, 0]
    """

    try:
        scores = scores_input(students)
        scores = convert_to_list(students, scores)

    except ValueError:
        print("Scores must only include whole-number integer values between 0-100.")
        scores = get_scores(students)

    except IndexError:
        print("Scores contains the incorrect amount space-separated values for each student. "
              + "Please provide a minimum of " + str(students) + " values.")
        scores = get_scores(students)

    return scores


def scores_input(students):
    """
    Accepts user input, cleans, and validates spacing
    :param students: int value of students
    :return: String value user input; e.g. "100 70 50"
    """

    scores = input("Enter " + str(students) + " score(s): ").strip()

    spaces_count = scores.count(' ')
    score_breaks = students - 1
    if spaces_count < score_breaks:
        raise IndexError
    else:
        return scores


def convert_to_list(students, scores_str):
    """
    Processes conversion of values and creates grade scale
    :param scores_str: Space-separated integers within a String; e.g. "100 70 50"
    :param students: int quantity of students
    :return:  List[] containing int scores; e.g. [100, 0]
    """

    scores_list = scores_str.split()
    scores_list = list(map(int, scores_list))
    scores_list = scores_list[slice(students)]

    for current_score in scores_list:
        if current_score not in range(0, 101):
            raise ValueError

    return scores_list


def get_grade_scale(scores):
    """
    Create weighted grade scale & append to provided scores
    :param scores: List[] containing int scores; e.g. [100, 0]
    :return: Dict{} containing A-F minimum scores; e.g. {A:90, B:80, C:70, D:60, F:59}
    """

    best_score = max(scores)

    grading_scale = {'A': best_score - 10,
                     'B': best_score - 20,
                     'C': best_score - 30,
                     'D': best_score - 40,
                     'F': best_score - 41}

    return grading_scale


def output(scores, grade_scale):
    """
    Console-level output of students' scores & letter grades
    :param scores: List[] containing int scores; e.g. [100, 0]
    :param grade_scale: Dict{} containing A-F minimum scores; e.g. {A:90, B:80, C:70, D:60, F:59}
    :return: None
    """

    iteration = 1
    for current_score in scores:
        match current_score:
            case value if value in range(grade_scale.get('A'), (max(scores) + 1)):
                current_grade = 'A'
            case value if value in range(grade_scale.get('B'), grade_scale.get('A')):
                current_grade = 'B'
            case value if value in range(grade_scale.get('C'), grade_scale.get('B')):
                current_grade = 'C'
            case value if value in range(grade_scale.get('D'), grade_scale.get('C')):
                current_grade = 'D'
            case _:
                current_grade = 'F'

        print("Student " + str(iteration) + " score is " + str(current_score) + " and grade is " + current_grade)
        iteration += 1


main()
