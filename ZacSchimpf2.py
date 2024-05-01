"""
    Zac Schimpf
    CSCI 1620 001/851
    Professor Owora
    Week 02 - Lab 02
    29/01/2024
"""


class Grader:
    def __init__(self) -> None:
        """
        Main logic structure that accepts students & _scores, creates grade scale, and prints results
        """
        self.students = None
        self._scores = None
        self._grade_scale = None

        self.get_students()
        self.set_scores()
        self.set_grade_scale()

        print(self.__str__())

    def get_students(self) -> None:
        """
        Sets quantity of students
        """

        self.students = input("Total number of students: ").strip()
        try:
            self.students = int(self.students)

            if self.students < 0:
                raise IndexError

        except IndexError:
            print("\"" + str(self.students) + "\" must be a positive whole-number integer value")
            self.get_students()

        except ValueError:
            print("\"" + str(self.students) + "\" must be a whole-number integer value, please try again.")
            self.get_students()

    def set_scores(self) -> None:
        """
        Requests input of score and appends letter grade scale
        """

        try:
            self.scores_input()
            self.convert_to_list()

        except ValueError:
            print("Scores must only include whole-number integer values between 0-100.")
            self.set_scores()

        except IndexError:
            print("Scores contains the incorrect amount space-separated values for each student. "
                  + "Please provide a minimum of " + str(self.students) + " values.")
            self.set_scores()

    def scores_input(self) -> None:
        """
        Accepts user input, cleans, and validates spacing
        """

        self._scores = input("Enter " + str(self.students) + " score(s): ").strip()

        spaces_count = self._scores.count(' ')
        score_breaks = self.students - 1
        if spaces_count < score_breaks:
            raise IndexError

    def convert_to_list(self):
        """
        Processes conversion of values and creates grade scale
        """

        scores_list = self._scores.split()
        scores_list = list(map(int, scores_list))
        scores_list = scores_list[slice(self.students)]

        for current_score in scores_list:
            if current_score not in range(0, 101):
                raise ValueError

        self._scores = scores_list

    def set_grade_scale(self) -> None:
        """
        Create weighted grade scale & append to provided _scores
        """

        best_score = max(self._scores)

        self._grade_scale = {'A': best_score - 10,
                             'B': best_score - 20,
                             'C': best_score - 30,
                             'D': best_score - 40,
                             'F': best_score - 41}

    def __str__(self) -> str:
        """
        Console-level output of students' _scores & letter grades
        :return: String formatted data
        """

        output = ""
        iteration = 1

        for current_score in self._scores:
            match current_score:
                case value if value in range(self._grade_scale.get('A'), (max(self._scores) + 1)):
                    current_grade = 'A'
                case value if value in range(self._grade_scale.get('B'), self._grade_scale.get('A')):
                    current_grade = 'B'
                case value if value in range(self._grade_scale.get('C'), self._grade_scale.get('B')):
                    current_grade = 'C'
                case value if value in range(self._grade_scale.get('D'), self._grade_scale.get('C')):
                    current_grade = 'D'
                case _:
                    current_grade = 'F'

            output += ("Student " + self._scores.index(current_score) + " score is " + str(
                current_score) + " and grade is " + current_grade
                       + "\n")
            iteration += 1

        return output


test = Grader()
