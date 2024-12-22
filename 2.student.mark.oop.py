
import os
class Student:
    def __init__(self,id,name,dob):
        self._id=id
        self._name=name
        self._dob=dob
        self._mark={}
    def getmark(self,course,mark):
        self._mark[course]=mark
    def getid(self):
        return self._id
    def getname(self):
        return self._name
    def getdob(self):
        return self._dob
    def display(self):
        print(f"ID:{self._id}   Name: {self._name}  DoB: {self._dob}")
        if self._mark!={}:
            for course in self._mark:
                print(f"Course: {course}   Mark:{self._mark[course]}")
        else:
            print("No information")
        print("")
class StudentManagement:
    def __init__(self):
        self._student=[]
    def input_student(self):
        id=input("Enter student id: ")
        name=input("Enter student name: ")
        dob=input("Enter day of birth of student in form (DD/MM/YYYY): ")
        st=Student(id,name,dob)
        self._student.append(st)
        print("Add student successfully")
    def get_list_student(self):
        return self._student
    def show_list_student(self):
        for st in self._student:
            print(f"ID: {st.getid()}  Name: {st.getname()}  Dob: {st.getdob()} ")
    def input_mark(self):
        course=input("Enter course name to get mark : ")
        for st in self._student:
            print(f"ID:{st.getid()} Student:{st.getname()}")
            mark=input(f"Enter mark for {course} course: ")
            st.getmark(course,mark)
def menu():
    print("""
    ----------------------------
    1. Add Student
    2. List Student
    3. Get mark
    4. List mark
    5. Clear screen
    6. Exit
    ----------------------------""")    
def main():
    sm=StudentManagement()
    while(True):
        menu()
        n=int(input("Enter option:  "))
        if n in[1,2,3,4,5,6]:
            if n==1:
                sm.input_student()
            if n==2:
                sm.show_list_student()
            if n== 3:
                sm.input_mark()
            if n==4:
                for st in sm.get_list_student():
                    st.display()
            if n==5:
                os.system("cls")
            if n==6:
                break    
if __name__=="__main__":
    main()