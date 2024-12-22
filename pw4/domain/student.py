#CLASS
import numpy as np
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
    def get_mark(self):
        return self._mark
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
