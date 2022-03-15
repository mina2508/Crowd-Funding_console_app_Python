from projectsMenu import showProjMenu
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phoneregex=r'^01[0125][0-9]+'
email=""
password=""
id=0
def CheckUser(email,passwd):
       try:
            with open("users.txt",'r') as usersFile:
                  allUsers=usersFile.readlines()
                  for l in allUsers:
                        if l.split(":")[3]==email and l.split(":")[4]==passwd:
                           global id
                           id=l.split(":")[0] 
                           usersFile.seek(0)   
                           usersFile.close()  
                           return False
                  usersFile.close()      
            return True
       except Exception as e:
               return True



def login():
    flag=0
    while flag==0:
        while True:
            global email
            email=input("please enter the Email to log : ")
            if (re.fullmatch(regex,email)):
                break
            else:
               print("-----Not Valid email---") 
        while True:
            global password
            password=input("please enter the Password to log in ")
            if (len(password)>=4):
                break
            else:
                print("-----password is least 4 characters---")             
        if CheckUser(email,password):
           print("-----you have entered wroong email or password---")
        else:
             flag=1
             print("--logged in successfully---")
             userid=str(id)
             return showProjMenu(userid)
            
                    