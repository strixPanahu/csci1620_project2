import tkinter
from tkinter import OptionMenu, Entry, Button, StringVar, Label, END, TclError


class GUI(tkinter.Tk):
    def __init__(self) -> None:
        """
        Grader GUI framework & landing page
        """
        super().__init__()

        self.title("CSCI 1620 - Project 2")
        self.height = 180
        self.geometry("240x" + str(self.height))
        self.resizable(False, False)

        self.user_input = []
        self.error = None
        self.error_code = None
        self.ERROR_MESSAGES = None

        self.name_label = Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name = StringVar(self)
        self.name_entry = Entry(self, textvariable=self.name)
        self.name_entry.grid(row=0, column=1, columnspan=1)

        self.attempts_label = Label(self, text="Attempts:")
        self.attempts_label.grid(row=1, column=0, padx=10, pady=10)
        self.attempts_options = [n for n in range(1, 5)]
        self.attempts_selection = StringVar(self)
        self.attempts_selection.set(str(self.attempts_options[0]))
        self.attempts_drop = OptionMenu(self, self.attempts_selection, *self.attempts_options)
        self.attempts_drop.grid(row=1, column=1)

        self._grade_label = Label(self, text="Grade 1:")
        self._grade_label.grid(row=2, column=0, padx=10, pady=10)
        self._grade = StringVar(self)
        self._grade_entry = Entry(self, textvariable=self._grade)
        self._grade_entry.grid(row=2, column=1, columnspan=1)

        self.save = Button(self, text="SUBMIT", command=self.refresh)
        self.save.grid(row=3, column=1, columnspan=1, padx=10, pady=10)

        self._grade_label_two = None
        self._grade_two = None
        self._grade_entry_two = None
        self._grade_label_three = None
        self._grade_three = None
        self._grade_entry_three = None
        self._grade_label_four = None
        self._grade_four = None
        self._grade_entry_four = None

        self.attempts_selection.trace('w', self.resize)

    def resize(self, *args) -> None:
        """
        Resize window after selecting an attempts value
        """

        self.height = 150 + int(self.attempts_selection.get()) * 35
        self.geometry("240x" + str(self.height))

        try:
            self._grade_label_two.destroy()
            self._grade_two = StringVar(self)
            self._grade_entry_two.destroy()
        except AttributeError:
            pass  # ignore, if entry DNE
        try:
            self._grade_label_three.destroy()
            self._grade_three = StringVar(self)
            self._grade_entry_three.destroy()
        except AttributeError:
            pass  # ignore, if entry DNE
        try:
            self._grade_label_four.destroy()
            self._grade_four = StringVar(self)
            self._grade_entry_four.destroy()
        except AttributeError:
            pass  # ignore, if entry DNE
        try:
            self.error_code = 0
            self.error.destroy()
        except AttributeError:
            pass  # ignore, if error DNE

        if 1 < int(self.attempts_selection.get()):
            self._grade_label_two = Label(self, text="Grade 2:")
            self._grade_label_two.grid(row=3, column=0, padx=10, pady=10)
            self._grade_two = StringVar(self)
            self._grade_entry_two = Entry(self, textvariable=self._grade_two)
            self._grade_entry_two.grid(row=3, column=1, columnspan=1)
        if 2 < int(self.attempts_selection.get()):
            self._grade_label_three = Label(self, text="Grade 3:")
            self._grade_label_three.grid(row=4, column=0, padx=10, pady=10)
            self._grade_three = StringVar(self)
            self._grade_entry_three = Entry(self, textvariable=self._grade_three)
            self._grade_entry_three.grid(row=4, column=1, columnspan=1)
        if 3 < int(self.attempts_selection.get()):
            self._grade_label_four = Label(self, text="Grade 4:")
            self._grade_label_four.grid(row=5, column=0, padx=10, pady=10)
            self._grade_four = StringVar(self)
            self._grade_entry_four = Entry(self, textvariable=self._grade_four)
            self._grade_entry_four.grid(row=5, column=1, columnspan=1)

        save_row = int(self.attempts_selection.get()) + 2
        self.save.grid(row=save_row, column=1, columnspan=1, padx=10, pady=10)

    def refresh(self) -> None:
        """
        Reload window after selecting the "Enter" button
        """
        try:
            self.error_code = 0
            self.error.destroy()
        except AttributeError:
            pass  # ignore, if error DNE

        self.get_grade()
        self.get_name()
        if self.error_code != 0:
            if self.height != 190 + int(self.attempts_selection.get()) * 35:
                self.height = 190 + int(self.attempts_selection.get()) * 35
                self.geometry("240x" + str(self.height))

            self.error = Label(self, text=self.get_error_code())
            error_row = int(self.attempts_selection.get()) + 2
            self.error.grid(row=error_row, column=0, columnspan=2, padx=10, pady=10)

            if self.error_code == -3:
                self.error.config(fg="#D74826")
            if self.error_code == -2:
                self.error.config(fg="#FF69B4")
            if self.error_code == -1:
                self.error.config(fg="#ED7117")

            save_row = int(self.attempts_selection.get()) + 3
            self.save.grid(row=save_row, column=1, columnspan=1, padx=10, pady=10)
        else:  # save & export vals
            if self.height != 150 + int(self.attempts_selection.get()) * 35:
                self.height = 150 + int(self.attempts_selection.get()) * 35
                self.geometry("240x" + str(self.height))

            self.user_input.append([self.get_name(), self.get_grade()])

        try:
            self._grade_entry.delete(0, END)
            self.name_entry.delete(0, END)
            self._grade_entry_two.delete(0, END)
            self._grade_entry_three.delete(0, END)
            self._grade_entry_four.delete(0, END)
        except (AttributeError, TclError):
            pass  # ignore, if error DNE

    def get_name(self) -> str:
        """
        Get data from the Name entry
        :return: str value entered in name field, else returns empty str
        """
        if self.name.get() != "":
            return self.name.get().strip()
        else:
            self.error_code = -3
            return ""

    def get_grade(self) -> list:
        """
        Get data from the Grade entry
        :return: list of positive ints if good, else returns error code
        """
        try:
            if self._grade.get() != "":
                grade = int(self._grade.get().strip())
                if grade not in range(0, 101):
                    raise ValueError

                grade_two = None
                if 1 < int(self.attempts_selection.get()):
                    grade_two = int(self._grade_two.get().strip())
                    if grade_two not in range(0, 101):
                        raise ValueError

                grade_three = None
                if 2 < int(self.attempts_selection.get()):
                    grade_three = int(self._grade_three.get().strip())
                    if grade_three not in range(0, 101):
                        raise ValueError

                return [grade, grade_two, grade_three]
            else:
                raise UnboundLocalError

        except UnboundLocalError:
            self.error_code = -1
        except ValueError:
            self.error_code = -2
        return []

    def get_user_input(self) -> list:
        """
        :return: List[] of each grade percentage
        """
        return self.user_input

    def get_error_code(self) -> str:
        """
        :return: Str containing the currently raised error code
        """
        self.ERROR_MESSAGES = ["Name must not be blank", "Grade must be between 0-100.", "Enter correct grade value"]
        return self.ERROR_MESSAGES[self.error_code]
