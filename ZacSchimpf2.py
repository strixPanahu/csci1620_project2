"""
    Zac Schimpf
    CSCI 1620 001/851
    Professor Owora
    Final - Project 2
    29/4/2024
"""
from csv import writer
from statistics import median, mean
import gui


class Grader:
    def __init__(self, scores) -> None:
        """
        Main logic structure that accepts students & scores, creates grade scale, and prints results
        """
        self._scores = scores
        self._grade_scale = self.set_grade_scale()
        self.output_to_csv()

    def set_grade_scale(self) -> dict:
        """
        Create weighted grade scale & append to provided _scores
        :return Dict containing A, B, C, D, & F percentage cutoffs
        """

        best_score = max(self._scores)

        return {'A': best_score - 10,
                'B': best_score - 20,
                'C': best_score - 30,
                'D': best_score - 40,
                'F': best_score - 41}

    def get_letter_grade(self, grade) -> str:
        """
        Retrieve weighted letter grade for provided grade percentage
        """
        match grade:
            case value if value in range(self._grade_scale.get('A'), (max(self._scores) + 1)):
                grade = 'A'
            case value if value in range(self._grade_scale.get('B'), self._grade_scale.get('A')):
                grade = 'B'
            case value if value in range(self._grade_scale.get('C'), self._grade_scale.get('B')):
                grade = 'C'
            case value if value in range(self._grade_scale.get('D'), self._grade_scale.get('C')):
                grade = 'D'
            case _:
                grade = 'F'

        return grade

    def output_to_csv(self):
        """
        Write a List[{}, {}] to a csv file in the current working directory, named output.csv
        :return None
        """

        outbound_name = "output.csv"

        with open(outbound_name, 'w', newline='') as outbound_file:
            csv_writer = writer(outbound_file, delimiter=',')
            for current_score in self._scores:
                csv_writer.writerow(["Student " + str(self._scores.index(current_score) + 1),
                                     current_score,
                                     self.get_letter_grade(current_score)])
            csv_writer.writerow(["Median", median(self._scores)])
            csv_writer.writerow(["Mean", mean(self._scores)])

    def __str__(self) -> str:
        """
        Console-level output of students' _scores & letter grades
        :return: String formatted data
        """

        output = ""

        for current_score in self._scores:
            output += ("Student " + str(self._scores.index(current_score) + 1) + " score is " + str(current_score)
                       + " and grade is " + self.get_letter_grade(current_score) + "\n")

        return output


if __name__ == "__main__":
    app = gui.GUI()
    app.mainloop()

    grades = Grader(app.get_user_input())
    print(grades.__str__())
