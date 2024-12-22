#MAIN
import os
import curses
from domain.student import Student
from input import input_student, input_mark, input_credit_for_course
from output import show_list_student, sort_gpa, display
class StudentManagement:
    def __init__(self):
        self._student=[]
    def add_student(self,student):
        self._student=student
    def get_list_student(self):
        return self._student
def main_menu(stdscr):
    sm = StudentManagement()
    curses.cur_set=(0)
    current_option=1
    menu=["|-------------------|","| 1. Add Student    |","| 2. List Students  |","| 3. Enter Marks    |","| 4. List Marks     |","| 5. Enter Credits  |","| 6. List GPA       |","| 7. Clear Screen   |","| 8. Exit           |","|-------------------|"]
    while True:
        stdscr.clear()
        for idx, option in enumerate(menu):
            if idx == current_option:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(idx + 1, 2, option)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 1, 2, option)

        stdscr.refresh()
        n = stdscr.getch()

        if n == curses.KEY_UP and current_option > 1:
            current_option -= 1
        elif n == curses.KEY_DOWN and current_option < len(menu) - 2:
            current_option += 1
        elif n == ord('\n'):  # Enter key
            if menu[current_option] == "| 1. Add Student    |":
                student=input_student(stdscr,sm.get_list_student())
                sm.add_student(student)
            elif menu[current_option] == "| 2. List Students  |":
                show_list_student(stdscr,sm.get_list_student())
            elif menu[current_option] == "| 3. Enter Marks    |":
                input_mark(stdscr,sm.get_list_student())
            elif menu[current_option] == "| 4. List Marks     |":
                for st in sm.get_list_student():
                    display(stdscr,st.getid(),st.getname(),st.getdob(),st.get_mark())
            elif menu[current_option] == "| 5. Enter Credits  |":
                input_credit_for_course(stdscr,sm.get_list_student())
            elif menu[current_option] == "| 6. List GPA       |":
                sort_gpa(stdscr,sm.get_list_student())
            elif menu[current_option] == "| 7. Clear Screen   |":
                os.system("cls" if os.name == "nt" else "clear")
            elif menu[current_option] == "| 8. Exit           |":
                break

def main():
    curses.wrapper(main_menu)

if __name__ == "__main__":
    main()
