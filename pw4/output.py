#OUTPUT
def show_list_student(stdscr,student):#2
    y=11
    for st in student:
        stdscr.addstr(y,0,f"ID: {st.getid()}  Name: {st.getname()}  Dob: {st.getdob()} ")
        y+=1
    stdscr.refresh()
    stdscr.getch()
def sort_gpa(stdscr,student):#6
    y=11
    for st in student:
        st.cal_gpa()
    student.sort(key=lambda st: st.getgpa(),reverse=True)
    stdscr.addstr(y,0,'List student after sorted: ')
    y+=1
    for st in student:
        stdscr.addstr(y,0,f"ID: {st.getid()}     Name: {st.getname()}      GPA: {st.getgpa()}")
        y+=1
    stdscr.refresh()
    stdscr.getch()
def display(stdscr,id,name,dob,mark):#4
    y=11
    stdscr.addstr(y,0,f"ID:{id}   Name: {name}  DoB: {dob}")
    y+=1
    if mark!={}:
        for course in mark:
            stdscr.addstr(y,0,f"Course: {course}   Mark:{mark[course]}")
            y+=1
    else:
        stdscr.addstr("No information")
        y+=1
    stdscr.addstr("")
    stdscr.refresh()
    stdscr.getch()