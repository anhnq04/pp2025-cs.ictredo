#INPUT
from math import floor
from domain.student import Student
def input_student(stdscr,student):#1
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
    student.append(st)
    stdscr.addstr(y,0,"Add student successfully")
    stdscr.refresh()
    stdscr.getch()
    return student


def input_mark(stdscr,student):#3
    y=11
    stdscr.addstr(y,0,"Enter course name to get mark : ")
    course=stdscr.getstr().decode('utf-8')
    stdscr.addstr(y,len("Enter course name to get mark : "),course)
    y+=1
    for st in student:
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

def input_credit_for_course(stdscr,student):#5
    y=11
    for st in student:
        if st==student[0]:
            st.inputcredit(stdscr)
            y+=1
            cd=st.getcredit()
        else:
            st.copy_credit(cd)
        stdscr.addstr(y,0,f"Add credit successfully fo student id: {st.getid()} ")
        y+=1
        stdscr.refresh()
        stdscr.getch()
