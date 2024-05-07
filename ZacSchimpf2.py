from csv import writer
from statistics import median, mean
import gui


class Grader:
    def __init__(self, scores) -> None:
        """
        Main logic structure that accepts students & scores, creates grade scale, and prints results
        """
        self._all_scores = scores
        self._highest_scores = []

        self.set_highest_scores()
        self._grade_scale = self.set_grade_scale()
        self.output_to_csv()

    def set_highest_scores(self):
        """
        Parse student scores and set the highest attempt
        """
        for student in self._all_scores:
            self._highest_scores.append(max([score for score in student[1] if score is not None]))

    def set_grade_scale(self) -> dict:
        """
        Create weighted grade scale & append to provided _scores
        :return Dict containing A, B, C, D, & F percentage cutoffs
        """

        best_score = max(self._highest_scores)

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
            case value if value in range(self._grade_scale.get('A'), (max(self._highest_scores) + 1)):
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
            csv_writer.writerow(["Name", "Score 1", "Score 2", "Score 3", "Score 4"])
            for current_score in self._all_scores:
                csv_writer.writerow([current_score[0]] + current_score[1])
            csv_writer.writerow(["Median", median(self._highest_scores)])
            csv_writer.writerow(["Mean", mean(self._highest_scores)])

    def __str__(self) -> str:
        """
        Console-level output of students' _scores & letter grades
        :return: String formatted data
        """

        output = ""

        index = 0
        for current_score in self._highest_scores:
            output += (self._all_scores[index][0] + "\'s score is " + str(current_score)
                       + " and grade is " + self.get_letter_grade(current_score) + "\n")
            index += 1

        return output


if __name__ == "__main__":
    app = gui.GUI()
    app.mainloop()

    grades = Grader(app.get_user_input())
    print(grades.__str__())
