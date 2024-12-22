import os
from math import floor
import numpy as np
import curses
class Student:
    def __init__(self,id,name,dob):
        self._id=id
        self._name=name
        self._dob=dob
        self._gpa=0
        self._mark={}
        self._credit={}
    def getmark(self,course,mark):
        self._mark[course]=mark
    def inputcredit(self,stdscr):
        y=11
        for c in list(self._mark.keys()):
            stdscr.addstr(y,0,f"Enter the credit for {c} course: ")
            credit=int(stdscr.getstr().decode('utf-8'))
            stdscr.addstr(y,len("Enter the credit for  course: ")+len(c),str(credit))
            stdscr.refresh()
            self._credit[c]=credit   
            stdscr.refresh()
            stdscr.getch()
    def getcredit(self):
        return self._credit 
    def copy_credit(self,cd):
        self._credit=cd     
    def getid(self):
        return self._id
    def getname(self):
        return self._name
    def getdob(self):
        return self._dob
    def getgpa(self):
        return self._gpa
    def cal_gpa(self):
        if not self._mark or not self._credit:
            self._gpa=0
            return self._gpa
        else:
            mark=np.array(list(self._mark.values()))
            credit=np.array(list(self._credit.values()))
            sum=np.sum(mark*credit)
            tc=np.sum(credit)
            self._gpa=round(sum/tc,1)
            return self._gpa    
    def display(self,stdscr):
        y=11
        stdscr.addstr(y,0,f"ID:{self._id}   Name: {self._name}  DoB: {self._dob}")
        y+=1
        if self._mark!={}:
            for course in self._mark:
                stdscr.addstr(y,0,f"Course: {course}   Mark:{self._mark[course]}")
                y+=1
        else:
            stdscr.addstr("No information")
            y+=1
        stdscr.addstr("")
        stdscr.refresh()
        stdscr.getch()

    
class StudentManagement:
    def __init__(self):
        self._student=[]
    def input_student(self,stdscr):
        y=11
        stdscr.addstr(y,0,"Enter student id: ")
        id=stdscr.getstr().decode('utf-8')       
        stdscr.addstr(y,len("Enter student id: "),id)
        stdscr.refresh()
        y+=1
        stdscr.addstr(y,0,"Enter student name: ")
        name=stdscr.getstr().decode('utf-8')
        stdscr.addstr(y,len("Enter student name: "),name)
        stdscr.refresh()
        y+=1
        stdscr.addstr(y,0,"Enter day of birth of student in form (DD/MM/YYYY): ")
        dob=stdscr.getstr().decode('utf-8')
        stdscr.addstr(y,len("Enter day of birth of student in form (DD/MM/YYYY): "),dob)
        stdscr.refresh()
        y+=1
        st=Student(id,name,dob)
        self._student.append(st)
        stdscr.addstr(y,0,"Add student successfully")
        y+=1
        stdscr.refresh()
        stdscr.getch()
    def get_list_student(self):
        return self._student
    def show_list_student(self,stdscr):
        y=11
        for st in self._student:
            stdscr.addstr(y,0,f"ID: {st.getid()}  Name: {st.getname()}  Dob: {st.getdob()} ")
            y+=1
        stdscr.refresh()
        stdscr.getch()
    def input_mark(self,stdscr):
        y=11
        stdscr.addstr(y,0,"Enter course name to get mark : ")
        course=stdscr.getstr().decode('utf-8')
        stdscr.addstr(y,len("Enter course name to get mark : "),course)
        y+=1
        for st in self._student:
            stdscr.addstr(y,0,f"ID:{st.getid()} Student:{st.getname()}")
            y+=1
            stdscr.addstr(y,0,f"Enter mark for {course} course: ")
            mark=float(stdscr.getstr().decode('utf-8'))
            mark=floor(mark*10)/10
            stdscr.addstr(y,len(f"Enter mark for  course: ")+len(course),str(mark))
            stdscr.refresh()
            y+=1
            st.getmark(course,mark)
        stdscr.addstr(y,0,"Add student successfully!")
        y+=1
        stdscr.refresh()
        stdscr.getch()
    def input_credit_for_course(self,stdscr):
        y=11
        for st in self._student:
            if st==self._student[0]:
                st.inputcredit(stdscr)
                y+=1
                cd=st.getcredit()
            else:
                st.copy_credit(cd)
            stdscr.addstr(y,0,f"Add credit successfully fo student id: {st.getid()} ")
            y+=1
            stdscr.refresh()
            stdscr.getch()
            
    def sort_gpa(self,stdscr):
        y=11
        for st in self._student:
            st.cal_gpa()
        self._student.sort(key=lambda st: st.getgpa(),reverse=True)
        stdscr.addstr(y,0,'List student after sorted: ')
        y+=1
        for st in self._student:
            stdscr.addstr(y,0,f"ID: {st.getid()}     Name: {st.getname()}      GPA: {st.getgpa()}")
            y+=1
        stdscr.refresh()
        stdscr.getch()

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
                sm.input_student(stdscr)
            elif menu[current_option] == "| 2. List Students  |":
                sm.show_list_student(stdscr)
            elif menu[current_option] == "| 3. Enter Marks    |":
                sm.input_mark(stdscr)
            elif menu[current_option] == "| 4. List Marks     |":
                for st in sm.get_list_student():
                    st.display(stdscr)
            elif menu[current_option] == "| 5. Enter Credits  |":
                sm.input_credit_for_course(stdscr)
            elif menu[current_option] == "| 6. List GPA       |":
                sm.sort_gpa(stdscr)
            elif menu[current_option] == "| 7. Clear Screen   |":
                os.system("cls" if os.name == "nt" else "clear")
            elif menu[current_option] == "| 8. Exit           |":
                break

def main():
    curses.wrapper(main_menu)

if __name__ == "__main__":
    main()
