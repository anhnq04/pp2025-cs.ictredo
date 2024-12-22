import os
Student=[]
Course=[]
mark={}
while(True):
    print("""
    menu()
    1.Add Student
    2.Add Course
    3.Get Mark
    4.Print
    5.Clear screen
    6.Exit
""")
    n=int(input("enter option: "))
    if n in [1,2,3,4,5,6]:
        if n==1:
            s_id=input("Student's id: ")
            sname=input("Student's name: ")
            dob=input("Day of birth(DD/MM/YYYY): ")
            Student.append({'id':s_id, 'name':sname,'Day of Birth':dob})
        elif n==2:
            c_id=input("Course's id: ")
            cname=input("Course's name: ")
            Course.append({'id':c_id, 'name':cname})
        elif n==3:
            course_id=input("pls input the course id: ")
            for c in Course:
                if course_id==c['id']:
                    for s in Student:
                            print(f"Enter mark for Student:{s['name']},ID:{s['id']}: ")
                            marks =float(input())
                            if 0<=marks<=20:
                                mark[s['id']]=marks
                            else:
                                print("Enter a valid mark in range 0-20")
        elif n==4:
            c_id=input("Enter course id to get mark: ")
            for c in Course:
                if c_id==c['id']:
                    getmark=mark.get(c_id,{})
                    if getmark=={}:
                        print("no mark in this course ")
                    else:
                        for s in Student:
                            st_id=s['id']
                            ma=mark.get(st_id,'No mark')
                            print(f"Course ID:{c_id}, Student:{s['name']}, ID:{st_id}, Mark:{ma}")
        elif n==5:
            os.system('cls')
        else:
            print("End task")
            break
    else:
        print("invalid n")



    
        

