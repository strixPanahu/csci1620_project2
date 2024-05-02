from csv import writer
import tkinter
from tkinter import ttk


class GUI(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Project 2")
        self.height = "80"
        self.geometry("240x" + self.height)
        self.resizable(False, False)

        self.user_input = []
        self.error_one = None

        self.grade_label = tkinter.ttk.Label(self, text="Grade:")
        self.grade_label.grid(row=0, column=0, padx=10, pady=10)
        self.grade = tkinter.StringVar(self)
        self.grade_entry = tkinter.ttk.Entry(self, textvariable=self.grade)
        self.grade_entry.grid(row=0, column=1, columnspan=3)

        self.save = tkinter.ttk.Button(self, text="ENTER", command=self.refresh)
        self.save.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    def refresh(self):
        try:
            self.error_one.destroy()
        except AttributeError:
            pass  # ignore, if error DNE

        grade = self.get_grade()
        if grade < 0:  # if error code exists
            if self.height != "120":
                self.height = "120"
                self.geometry("240x" + self.height)

            self.error_one = tkinter.Label(self, text=self.get_error_code(grade))
            self.error_one.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        else:  # save & export vals
            if self.height != "80":
                self.height = "80"
                self.geometry("240x" + self.height)

            self.user_input.append(grade)

        self.grade_entry.delete(0, tkinter.END)

    def get_grade(self) -> int:
        """
        Get Entry field
        :return: int if good, else returns error code
        """

        try:
            if self.grade.get() != "":
                grade = int(self.grade.get().strip())

                if grade not in range(0, 101):
                    raise ValueError

                return grade
            else:
                raise UnboundLocalError

        except UnboundLocalError:
            return -1
        except ValueError:
            return -2

    def get_user_input(self):
        return self.user_input

    def get_error_code(self, error):
        match error:
            case -1:
                return "Enter correct grade value"
            case -2:
                return "Grade must be between 0-100."
