import os
import  pickle
import random
class Student_1:
    
    def __init__(self):
        self._fee=00
        self.std_attd=00
        self.tm=00


    def attendence(self,cls):
        if cls<=5:
            self.std_attd=random.randint(100,201)
            srattd="Attendance of "+str(self.std_attd)+"out of 200"
        elif cls>5:
            self.std_attd=random.randint(100,251)
            srattd="Attendance of "+str(self.std_attd)+"out of 250"
        return srattd
    def marks(self):
        self.tm=random.randint(50,100)
        return self.tm
    
        
    def fees(self,cls):
        self.std_class=int(cls[0:2])
        if self.std_class==1 :
            self._fee=30000
        elif self.std_class==2 :
            self._fee=34000
        elif self.std_class==3 :
            self._fee=35000
        elif self.std_class==4 :
            self._fee=35000
        elif self.std_class==5 :
            self._fee=40000
        elif self.std_class==6 :
            self._fee=40000
        elif self.std_class==7 :
            self._fee=42000
        elif self.std_class==8 :
            self._fee=42000
        elif self.std_class==9:
            self._fee=45000
        elif self.std_class==10 :
            self._fee=45000
        elif self.std_class==11 :
            self._fee=50000
        elif self.std_class==12 :
            self._fee=30000
        return self._fee
    def aes15(self):
        z=open("Annual exam15.txt","w+")
        return z.readline()
class Student_2:
    
    def __init__(self):
        self._fee=00
        self.std_attd=00
        self.tm=00


    def attendence(self,cls):
        if cls<=5:
            self.std_attd=random.randint(100,201)
            srattd="Attendance of "+str(self.std_attd)+"out of 200"
        elif cls>5:
            self.std_attd=random.randint(100,251)
            srattd="Attendance of "+str(self.std_attd)+"out of 250"
        return srattd
    def marks(self):
        self.tm=random.randint(50,100)
        return self.tm
    
        
    def fees(self,cls):
        self.std_class=int(cls[0:2])
        if self.std_class==1 :
            self._fee=30500
        elif self.std_class==2 :
            self._fee=34500
        elif self.std_class==3 :
            self._fee=35500
        elif self.std_class==4 :
            self._fee=35500
        elif self.std_class==5 :
            self._fee=40500
        elif self.std_class==6 :
            self._fee=40500
        elif self.std_class==7 :
            self._fee=42500
        elif self.std_class==8 :
            self._fee=42500
        elif self.std_class==9:
            self._fee=45500
        elif self.std_class==10 :
            self._fee=45500
        elif self.std_class==11 :
            self._fee=50500
        elif self.std_class==12 :
            self._fee=30500
        return self._fee
    def aes16(self):
        z=open("Annual exam16.txt","w+")
        return z.readline()

def ask_sess(klass):    
    print"Enter '1' for session 2015-16  :  "
    print"Enter '2' for session 2016-17  :  "
    ses=int(raw_input("Enter choice for the session"))
    if ses==1:
        print"Enter '1' for fees and other details of the student :  " 
        print"Enter '2' for Annual Exam schedule  :  "
        ch=int(raw_input("Enter choice according to your requirement:"))
        obj=Student_1()
        if ch==1:
            klas1=klass.student_class
            print obj.fees(klas1)  , "is your monthly fees"
            obj.attendence(klas1)
            print "marks obtained in last year annual exam",obj.marks()
        if ch ==2:
            print obj.aes15()
    if ses==2:
        print"Enter '1' for fees and other details of the student :  " 
        print"Enter '2' for Annual Exam schedule  :  "
        ch1=int(raw_input("Enter choice according to your requirement:"))
        obj=Student_2()
        if ch==1:
            klas1=klass.student_class
            print obj.fees(klas1)  , "is your monthly fees"
            obj.attendence(klas1)
            print "marks obtained in last year annual exam",obj.marks()
        if ch ==2:
            print obj.aes16()
        


class staff(object):
    def  __init__(self,ID,typeofstaff,subjectexpert="none" ):
        self.user_ID=ID
        self.typ=typeofstaff
        if self.user_ID :
            return True
        else:
            return False
    def salary(self):
        fin=open("salary.dat",r)
        return fin.readlines()
    def typestaff(self, type_of_staff):
        if self.typ=="Teaching":
            return self.subject_expert
        else:
            return "They ae non teaching /working staff"
    def qualification(self):
        if self.typ=="Teaching staff":
            print"Well Qualified with B.ED"
            print"Expert in ", self.subjectexpert
        else:
            print"Non teaching staff"
            print "Minimum Qualified is 12th pass"
    def duty(self,ID):
        self.user_ID=ID
        f2.open("duty.dat",r)
        while true:
            l1=f.readline()
            if l1[0:2:1]=="ID":
                print"duty",l1[0:2:1]
            else:
                print"Enter Valid user_ID"
    def joining(self):
        if self.user_ID in List:
            Dict.self.user_ID
        else:
            print"Enter Valid user_ID"
class teacher(staff):
    def  __init__(self,ID,exp,class1):
        self.user_ID=ID
        self.subexpert=exp
        self.classteacher=class1
        staff. __init__(self,ID)
    def academic(self,stud):
        f3=open("Student academic perfor.dat","a+")
        f4=open("salary.dat",r)
        while true:
            l1=f3.readline()
            if l1[0:2:1]==self.stud:
                return l1[0:2:1]
            else:
                print"Enter Valid Student"
    def classteacher(self,ID):
        l2=Dict2.ID
        print"Teacher is class teacher of ",l2
class management(staff):
    def __init__(self,ID,m=None):
        self.user_ID=ID
        self.management_ID=m
        staff. __init__(self,ID)
    def special(self,m):
        self.management=m
        f4=open("management.dat","r+")
        while true:
            l1=f4.readline
            if l1[0:2:1]==m:
                print"Special work",l1[3:4:1]
            else:
                print"No special work given"
    def head(self,m):
        self.management_ID=m
        l1=Dict2.m
        if l1 !="none":
            print"Head of Department ", l1
        else:
            print"Enter Valid management ID"
class Nonteaching(staff):
    def __init__(self,ID, wk):
        self.user_ID=ID
        self.work=wk
        staff. __init__(self,ID)
    def department(self,ID,wk):
        self.user_ID=ID
        self.work=wk
        f=open("Department of non teaching.dat", "r+")
        while true:
            l1=f.readline()
            if l1[0:2:1]==ID:
                print"Department", l1[2:5:1]
            else:
                print"No Department alloted"
                print"Enter valiiid Usert_ID"   

class id_creater:
    def __init__(self):
        self.student_name=" "
        self.student_dob=" "
        self.student_class=" "
        self.student_adno=0000
        self.user_id=" "
        self._password=00000000

    def assign_values(self,a,b,c,d):
        self.student_name=a
        self.student_dob=b
        self.student_class=c
        self.student_adno=d
        print "Congatulations!!! Registration for user id completed succesfully"

    def assign_user_id(self,str1,pass1):
        self.user_id=str1
        self._password=pass1
        print "User id :",self.user_id,"created"
    def open_id(self,str1):
        if str1==self._password:
            return 1
        else:
            return 0
class id_creater1:
    def __init__(self):
        self.s_name=" "
        self.s_dob=" "
        self.s_class=" "
        self.s_idno=0000
        self.user_id=" "
        self._password=00000000
    def assign_values(self,a,b,c,d):
        self.s_name=a
        self.s_dob=b
        self.s_class=c
        self.s_idno=d
        print "Congatulations!!! Registration for user id completed succesfully"
    def assign_user_id(self,str1,pass1):
        self.user_id=str1
        self._password=pass1
        print "User id :",self.user_id,"created"
    def open_id(self,str1):
        if str1==self._password:
            return 1
        else:
            return 0

def dumpfile(klass,str1):
    file_name=str1+".txt"
    fin=open(file_name,"w+")
    pickle.dump(klass,fin)
    fin.close()
    print "Registration done"

print"""

Hello user
please chose your id

STUDENT ------------ID.1
STAFF     -------------ID.2

"""
while True:
    try:
        while True :
            id_choice=int(raw_input("Please enter your choice as 1 or 2:"))
            if id_choice ==1 or id_choice==2:
                break
            else:
                print """Please Enter either 1 or 2"""
        break
    except :
        print "Please Enter either 1 or 2"

if id_choice==1:
    print"""
Hello student,
This is the official database of your school your can manange your data related to you and your school

Choices:
1.Login
2.Signup
"""
    while True:
        try:
            while True :
                choice=int(raw_input("Please enter your choice as 1 or 2:"))
                if choice ==1 or choice==2:
                    break
                else:
                    print """Please Enter either 1 or 2"""
            break    
        except :
            print "Please Enter either 1 or 2"
    if choice==1:
            user_id=raw_input("Enter your user id:")
            fout=open(user_id,"r+")  
            while True:
                try:
                    fin=fout  
                    stud=pickle.load(fin)
                    break
                except:    
                    fin.close()
            password = int(raw_input("please enter your password:"))
            pass_match=stud.open_id(password)
            while not pass_match:
                print "login failed due to incorrect pass word"
                password = int(raw_input("please enter your password:"))
                pass_match=stud.open_id(password)
            else:
                print "login succesfull"
            print """
Enter
1 - To modify or input your record
2 - To read your record"""
            my_choice=int(input("choice please:"))
            if my_choice==1:
                ask_sess(stud)
                
    if choice==2:
        print "Please fill up the following details" 
        a=raw_input("Your name:")
        b=raw_input("Your Date of birth (DD\MM\YYYY):")
        c=raw_input("Your class and section(class-section):")
        d=raw_input("Your admission number:")
        stud=id_creater()
        stud.assign_values(a,b,c,d)
        print "please enter one user id"
        str1=raw_input("user id:")
        while True:
            try:
                pass1=int(raw_input("Password (your password must have exactly 8 digits):"))
                if len(str(pass1))!=8:
                    raise ZeroDivisionError
                break
            except:
                print "please enter valid 8 digit numeric password"
        stud.assign_user_id(str1,pass1)
        dumpfile(stud,str1)
        print """
You have succesfully created your account now you can login to your accont by using
your user id also don't forget to end your user id with .txt extension
for example ;
                    if your id is anand7860 then enter it as anand7860.txt
Thank you for joining with us"""
if id_choice==2:
    print"""
Hello,
This is the official database of your school your can manange your data related to you and your school
 Enter
            1.Teaching staff
            2.Management
            3.Non-teaching staff


"""
    ch=input("enter your choice:")
    if ch==1:
        print"""Choices:
1.Login
2.Signup"""
        while True:
            try:
                while True :
                    choice=int(raw_input("Please enter your choice as 1 or 2"))
                    if choice ==1 or choice==2:
                        break
                    else:
                        print """Please Enter either 1 or 2"""
                break    
            except :
             print "Please Enter either 1 or 2"
        if choice==1:
            user_id=raw_input("Enter your user id:")
            fout=open(user_id,"r+")  
            while True:
                try:
                    fin=fout  
                    stud=pickle.load(fin)
                    break
                except:    
                    fin.close()
            password = int(raw_input("please enter your password:"))
            pass_match=stud.open_id(password)
            while not pass_match:
                print "login failed due to incorrect pass word"
                password = int(raw_input("please enter your password:"))
                pass_match=stud.open_id(password)
            else:
                print "login succesfull" 
    if choice==2:
        print "Please fill up the following details" 
        a=raw_input("Your name:")
        b=raw_input("Your Date of birth (DD\MM\YYYY):")
        c=raw_input("Class and section under you (class-section):")
        d=raw_input("Your staff id number:")
        stud=id_creater1()
        stud.assign_values(a,b,c,d)
        print "please enter one user id"
        str1=raw_input("user id:")
        while True:
            try:
                pass1=int(raw_input("Password (your password must have exactly 8 digits):"))
                if len(str(pass1))!=8:
                    raise ZeroDivisionError
                break
            except:
                print "please enter valid 8 digit numeric password"
        stud.assign_user_id(str1,pass1)
        dumpfile(stud1,str1)
        sub=raw_input("enter your expertise subject:")
        klas2=stud.s_class
        teach_obj=teacher(user_id,sub,klas2)
    if ch==2:
        while True:
            try:
                while True :
                    choice=int(raw_input("Please enter your choice as 1 or 2:"))
                    if choice ==1 or choice==2:
                        break
                    else:
                        print """Please Enter either 1 or 2"""
                break    
            except :
                 print "Please Enter either 1 or 2"
    if choice==1:
            user_id=raw_input("Enter your user id:")
            fout=open(user_id,"r+")  
            while True:
                try:
                    fin=fout  
                    stud=pickle.load(fin)
                    break
                except:    
                    fin.close()
            password = int(raw_input("please enter your password:"))
            pass_match=stud.open_id(password)
            while not pass_match:
                print "login failed due to incorrect pass word"
                password = int(raw_input("please enter your password:"))
                pass_match=stud.open_id(password)
            else:
                print "login succesfull" 
    if choice==2:
        print "Please fill up the following details" 
        a=raw_input("Your name:")
        b=raw_input("Your Date of birth (DD\MM\YYYY):")
        c=raw_input("Class and section under you (class-section):")
        d=raw_input("Your staff id number:")
        stud=id_creater1()
        stud.assign_values(a,b,c,d)
        print "please enter one user id"
        str1=raw_input("user id:")
        while True:
            try:
                pass1=int(raw_input("Password (your password must have exactly 8 digits):"))
                if len(str(pass1))!=8:
                    raise ZeroDivisionError
                break
            except:
                print "please enter valid 8 digit numeric password"
        stud.assign_user_id(str1,pass1)
        dumpfile(stud1,str1)
        m=raw_input("enter your management id:")
        manage_obj=management(user_id,m)
    if ch==3:
        wk=raw_input("enter your special  work:")
        non_obj=nonteaching
        print"""Choices:
1.Login
2.Signup"""
        
    while True:
        try:
            while True :
                choice=int(raw_input("Please enter your choice as 1 or 2:"))
                if choice ==1 or choice==2:
                    break
                else:
                    print """Please Enter either 1 or 2"""
            break    
        except :
             print "Please Enter either 1 or 2"
    if choice==1:
            user_id=raw_input("Enter your user id:")
            fout=open(user_id,"r+")
            print"""Choices:
1.Login
2.Signup"""
            while True:
                try:
                    fin=fout  
                    stud=pickle.load(fin)
                    break
                except:    
                    fin.close()
            password = int(raw_input("please enter your password:"))
            pass_match=stud.open_id(password)
            while not pass_match:
                print "login failed due to incorrect pass word"
                password = int(raw_input("please enter your password:"))
                pass_match=stud.open_id(password)
            else:
                print "login succesfull" 
    if choice==2:
        print "Please fill up the following details" 
        a=raw_input("Your name:")
        b=raw_input("Your Date of birth (DD\MM\YYYY):")
        c=raw_input("Class and section under you (class-section):")
        d=raw_input("Your staff id number:")
        stud=id_creater1()
        stud.assign_values(a,b,c,d)
        print "please enter one user id"
        str1=raw_input("user id:")
        while True:
            try:
                pass1=int(raw_input("Password (your password must have exactly 8 digits):"))
                if len(str(pass1))!=8:
                    raise ZeroDivisionError
                break
            except:
                print "please enter valid 8 digit numeric password"
        stud.assign_user_id(str1,pass1)
        dumpfile(stud1,str1)
