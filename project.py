
import mysql.connector as mys
import os
x=mys.connect(host='localhost',password='password',database='projectnew',user='root')

command=x.cursor(buffered=True)


def admin_portal():
    print(" ")
    print("college managment system")
    print("Enter 1 to register new student:")
    print("Enter 2 to register new teacher:")
    print("Enter 3 to modify salary of teacher:")
    print("Enter 4 to remove student:")
    print("Enter 5 to remove teacher:")
    print("Enter 6 to logout:")
    option1=int(input("enter the option:"))
    if option1==1:
        print('')
        print("student registration")
        privilage='student'
        try:
            studentuser=input("enter the student username:")
            studentpassword=input("enter the student password:")
            query=(studentuser,studentpassword,privilage)
            command.execute("INSERT INTO student (Name,password,privilage) VALUES(%s,%s,%s)",query)
            x.commit()
            print("The student has been successfully registered")
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            admin_portal()
        except:
            print('')
            print('creating table....')
            command.execute('CREATE TABLE student(Name varchar(20), password varchar(20), privilage varchar(20))')
            studentuser=input("enter the student username:")
            studentpassword=input("enter the student password:")
            query=(studentuser,studentpassword,privilage) # passing the values in the order of username , password and privilage
            command.execute("INSERT INTO student (Name,password,privilage) VALUES(%s,%s,%s)",query) 
            x.commit()
            print("The student has been successfully registered")
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            admin_portal()
    elif option1==2:
        print('')
        print("Teacher registration:")
        privilage='Teacher'
        try:   #if the table is present adding the values
            teacherusername=input("Enter the teacher username:")
            teacherpassword=input("Enter the teacher password:")
            teachersalary=input('Enter the salary of the teacher')
            query=(teacherusername,teacherpassword,privilage,teachersalary)
            command.execute('INSERT INTO teacher (Name,password,privilage,salary) VALUES(%s,%s,%s,%s)',query)
            x.commit()
            print("The teacher has been successfully registered")
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            admin_portal()
        except:# if the table is not present creating new table 
            print('Creating table...')
            command.execute('CREATE TABLE teacher(Name varchar(20), password varchar(20), privilage varchar(20), salary varchar(20))')
            teacherusername=input("Enter the teacher username:")
            teacherpassword=input("Enter the teacher password:")
            teachersalary=input('Enter the salary of the teacher')
            query=(teacherusername,teacherpassword,privilage,teachersalary)
            command.execute('INSERT INTO teacher (Name,password,privilage,salary) VALUES(%s,%s,%s,%s)',query)
            x.commit()
            print("The teacher has been successfully registered")
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            admin_portal()
    elif option1==3:
            print('')
            print('Modify teacher salary:')
            teachername=input("Enter the teacher name:")
            teachersalary=input("Enter the salary to be modified:")
            query=(teachername,)
            command.execute('SELECT * FROM teacher WHERE Name=%s',query)
            queryresult=command.fetchall()
            if len(queryresult)==0:
                print("The entred teacher name is not present for manupluation of salary")
                g=input("Enter 1 to go to teacher registration:")
                x2=list(g)
                for i in x2:
                    print("Teacher registration:")
                    privilage='Teacher'
                    teacherusername=input("Enter the teacher username:")
                    teacherpassword=input("Enter the teacher password:")
                    teachersalary=input('Enter the salary of the teacher:')
                    query=(teacherusername,teacherpassword,privilage,teachersalary)
                    command.execute('INSERT INTO teacher (Name,password,privilage,salary) VALUES(%s,%s,%s,%s)',query)
                    x.commit()
                    print("The teacher has been successfully registered")
                    print("********************************ST PETERS COLLEGE *********************")
                    print("********************************  ADMINISTRATION     *********************")
                    admin_portal()                                                                                                           


            else:
                value=(teachersalary,teachername)
                command.execute('UPDATE teacher SET salary=%s WHERE Name=%s',value) # modifiying  the salary of teacher
                x.commit()
                print("The salary has been successfully updated")
                print("********************************ST PETERS COLLEGE *********************")
                print("********************************  ADMINISTRATION     *********************")
                admin_portal()
        
    elif option1==4:
            print('')
            print('Student removal')
            studentname=input("Enter the student name:")
            query=(studentname,)
            command.execute('DELETE FROM student WHERE Name=%s',query) # checking if the student is present if present removed
            x.commit()
            if command.rowcount<1:
                print("The entered student is not present")
                print("********************************ST PETERS COLLEGE *********************")
                print("********************************  ADMINISTRATION     *********************")
                admin_portal()
            else:
                print(studentname+'has been removed')
                print("********************************ST PETERS COLLEGE *********************")
                print("********************************  ADMINISTRATION     *********************")
                admin_portal()
    elif option1==5: # to remove teacher 
        print('')
        print('Teacher removal')
        teachername=input("Enter the teacher name:")
        query=(teachername,)
        command.execute('DELETE FROM teacher WHERE Name=%s',query) #checking the if the teacher is present if present removed
        x.commit()
        if command.rowcount<1:
            print("The entered teacher is not present")
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            admin_portal()
        else:
            print(teachername+' has been removed')
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            admin_portal()
    elif option1==6:
        print('')
        print('sending to main console...')
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        main() 
    else:
        print('Invalid option')
def teacher_portal():
    print('')
    print('welcome to teacher portal')
    print('Enter 1 to Mark student register')
    print('Enter 2 to view register')
    print('Enter 3 to view teacher details')
    print('Enter 4 to logout ')
    option=int(input("Enter the option:"))
    if option==1:
        print('')
        print('Mark student register')
        command.execute("SELECT Name FROM student WHERE privilage='student'")
        studentrecords=command.fetchall()
        date=input(str("Enter the date in the manner DD//MM/YY:"))
        try:
            for i in studentrecords:
                i=str(i).replace("'","")
                i=str(i).replace(",","")
                i=str(i).replace("(","")
                i=str(i).replace(")","")
                status=input(str('status for '+str(i)+'P/A/L:'))
                queryvalues=(str(i),date,status)
                command.execute("INSERT INTO attendance1 (Name,date,status) VALUES(%s,%s,%s)",queryvalues)
                x.commit()
                print(i + '\t' "Marked as" '\t'  + status )
            print('successfully marked the register')
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            teacher_portal()
        except:
                print('')
                print('creating table...')
                command.execute('CREATE TABLE attendance1 (Name varchar(20), date varchar(20), status varchar(20))')
                for i in studentrecords:
                    i=str(i).replace("'","")
                    i=str(i).replace(",","")
                    i=str(i).replace("(","")
                    i=str(i).replace(")","")
                    status=input(str('status for '+str(i)+'P/A/L:'))
                    queryvalues=(str(i),date,status)
                    command.execute("INSERT INTO attendance1 (Name,date,status) VALUES(%s,%s,%s)",queryvalues)
                    x.commit()
                    print(i + '\t' "Marked as" '\t'  + status )
                print('successfully marked the register')
                print("********************************ST PETERS COLLEGE *********************")
                print("********************************  ADMINISTRATION     *********************")
                teacher_portal()
    elif option==2:
        print('')
        print('viewing student register')
        command.execute('SELECT*FROM attendance1')
        studentregister=command.fetchall()
        for i in studentregister:
            print('Name:',i[0])
            print('date:',i[1])
            print('status:',i[2])
        x.commit()
        print('successfull')
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        teacher_portal()
    elif option==3:
        print('')
        print('viewing Teacher details')
        command.execute('SELECT*FROM teacher')
        teacherlist=command.fetchall()
        for i in teacherlist:
            print('Name:',i[0])
            print('password:',i[1])
            print('privilage:',i[2])
            print('salary:',i[3])
        x.commit()
        print('successfull')
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        teacher_portal()
    elif option==4:
        print('')
        print('loging out...')
        print('sending to main console....')
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        main()

        
def teacher():
    print("")
    print("welcome to teacher login")
    print('')
    teacherusername1=input("Enter the teacher username:")
    teacherpassword1=input('Enter the teacher password:')
    query=(teacherusername1,teacherpassword1)
    command.execute('SELECT * FROM teacher WHERE Name=%s AND password=%s',query)
    queryresult=command.fetchall()
    print('The teacher details')
    for i in queryresult:
        if command.rowcount<=0:
            print("Invalid teacher login details")
            print('sending to teacher console...')
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            teacher()

        else:
            print('techer login')
            teacher_portal()
    x.commit()

def studentconsole():
    print("")
    print('Welcome to student console')
    print('Enter 1 to view register')
    print('Enter 2 to download register:')
    print('Enter 3 to view timetable:')
    print('Enter 4 to logout')
    option1=int(input("Enter the option:"))
    if option1==1:
        print('')
        print('Viewing the student register')
        studentusername=input('Enter the student username:')
        query=(studentusername,)
        command.execute('SELECT*FROM attendance1 WHERE Name=%s',query)
        studentlist=command.fetchall()
        for i in studentlist:
            print('Name:',i[0])
            print('date:',i[1])
            print('status:',i[2])
        x.commit()
        print('successfull')
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        studentconsole()
    elif option1==2:
        print('')
        print('Register download panel')
        studentusername=input('Enter the student username:')
        query=(studentusername,)
        command.execute('SELECT*FROM attendance1 WHERE Name=%s',query)
        studentlist=command.fetchall()
        f=open('register.txt','w')
        for i in studentlist:
            record=str(studentlist)
            f.write(record+'\n')
        f.close()
        print('The register has been successfully downloaded')
        x1=os.path.abspath("register.txt")
        print('The path of the download is:',x1)
        x.commit()
        print('successfull')
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        studentconsole()
    elif option1==3:
        print('')
        print('Time table portal')
        timetable1=int(input('Enter 1 to view the entire time table , Enter 2 to view the timetable of the specific day:'))
        if timetable1==1:
            try:
                print('')
                print('Viewing the entire time table')
                command.execute('SELECT*FROM timetable') 
                timetablelist=command.fetchall()
                for i in timetablelist:
                    print('Day:',i[0])       
                    print('subject1:',i[1])
                    print('subject2:',i[2])
                    print('subject3:',i[3])
                x.commit()
                print('successfull')
                print("********************************ST PETERS COLLEGE *********************")
                print("********************************  ADMINISTRATION     *********************")
                studentconsole()
            except:
                print('')
                print('creating table..')
                command.execute("CREATE TABLE timetable(day varchar(20),subject1 varchar(20), subject2 varchar(20), subject3 varchar(20))")
                command.execute("INSERT INTO timetable VALUES('Monday','computer','ai development','English')")
                command.execute("INSERT INTO timetable VALUES('Tuesday','Maths','web development','chemistry')")
                command.execute("INSERT INTO timetable VALUES('Wednesday','physics','chip encoding ','Maths')")
                command.execute("INSERT INTO timetable VALUES('Thursday','computer','Game development','English')")
                command.execute("INSERT INTO timetable VALUES('Friday','Chemistry','Robotics','physics')")
                print('Viewing the entire time table')
                command.execute('SELECT*FROM timetable') 
                timetablelist=command.fetchall()
                for i in timetablelist:
                    print('Day:',i[0])       
                    print('subject1:',i[1])
                    print('subject2:',i[2])
                    print('subject3:',i[3])
                x.commit()
                print('successfull')
                print("********************************ST PETERS COLLEGE *********************")
                print("********************************  ADMINISTRATION     *********************")
                studentconsole()
        
        if timetable1==2:
            try:
                print('')
                day=input('Enter the day for the respective time table:')
                query=(day,) 
                command.execute('SELECT*FROM timetable WHERE day=%s',query) 
                timetablelist=command.fetchall()
                for i in timetablelist:
                    print('Day:',i[0])       
                    print('subject1:',i[1])
                    print('subject2:',i[2])
                    print('subject3:',i[3])
                x.commit()
                print('successfull')
                print("********************************ST PETERS COLLEGE *********************")
                print("********************************  ADMINISTRATION     *********************")
                studentconsole()
            except:
                print('')
                print('creating table..')
                command.execute("CREATE TABLE timetable(day varchar(20),subject1 varchar(20), subject2 varchar(20), subject3 varchar(20))")
                command.execute("INSERT INTO timetable VALUES('Monday','computer','ai development','English')")
                command.execute("INSERT INTO timetable VALUES('Tuesday','Maths','web development','chemistry')")
                command.execute("INSERT INTO timetable VALUES('Wednesday','physics','chip encoding ','Maths')")
                command.execute("INSERT INTO timetable VALUES('Thursday','computer','Game development','English')")
                command.execute("INSERT INTO timetable VALUES('Friday','Chemistry','Robotics','physics')")
                print('')
                day=input('Enter the day for the respective time table:')
                query=(day,) 
                command.execute('SELECT*FROM timetable WHERE day=%s',query) 
                timetablelist=command.fetchall()
                for i in timetablelist:
                    print('Day:',i[0])       
                    print('subject1:',i[1])
                    print('subject2:',i[2])
                    print('subject3:',i[3])
                x.commit()
                print('successfull')
                print("********************************ST PETERS COLLEGE *********************")
                print("********************************  ADMINISTRATION     *********************")
                studentconsole()

    elif option1==4:
        print('')
        print('loging out...')
        print('sending to main console...')
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        main()
    else:
        print('')
        print('Invalid option')


def student():
    print('')
    print('Welcome to student login')
    studentname=input('Enter the student name:')
    studentpassword=input('Enter the student password:')
    privilage='student'
    queryvalue=(studentname,studentpassword,privilage)
    command.execute('SELECT*FROM student WHERE Name=%s AND password=%s AND privilage=%s',queryvalue)
    studentlist=command.fetchall()
    for i in studentlist:
        if command.rowcount<0:
            print('Invalid student login details')
            print('try again')
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            student()
        else:
            print('student login successfull')
            print('sending to student console....')
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            studentconsole()


def admin():
    print("")
    print("welcome admin")
    print("college managment system")
    username=input("Enter the admin username:")
    password=input("Enter the admin password:")
    if username=='admin1'and password=='password':
        print("You have logged in successfully")
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        admin_portal()
    else:
        redirect=input("The login details are wrong enter N to redirect back to home page:")
        if redirect=='N':
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            main()
        
def main():
    print(" Enter 1 for student login:")
    print("Enter 2 for teacher login:")
    print("Enter 3 for admin login:")
    print('Enter 4 to logout:')
    option=int(input('Enter the option:'))
    if option==1:
        print("STUDENT LOGIN")
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        student()
    if option==2:
        print("TEACHER LOGIN")
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        teacher()
    if option==3:
        print("ADMIN LOGIN")
        print("********************************ST PETERS COLLEGE *********************")
        print("********************************  ADMINISTRATION     *********************")
        admin()
    if option>3:
        print("invalid input")
        print('Enter x to close the terminal')
        print('Enter m to go back to the main console')
        x=input('Enter the option:')
        if x=='x':
            print('close')
        if x=='m':
            print("********************************ST PETERS COLLEGE *********************")
            print("********************************  ADMINISTRATION     *********************")
            main()


main()