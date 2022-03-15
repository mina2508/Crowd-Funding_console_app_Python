import login
import email
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phoneregex=r'^01[0125][0-9]+'

def getCheckUserEmail(email):
       try:
            with open("users.txt",'r') as usersFile:
                  allUsers=usersFile.readlines()
                  for l in allUsers:
                        if l.split(":")[3]==email:
                           usersFile.seek(0)   
                           usersFile.close()  
                           return False
                  usersFile.close()      
            return True
       except Exception as e:
               return True




def insertintoFile(ls):
   try:
    with open("users.txt",'r+') as usersFile:
            allUsers=usersFile.readlines()
            lastUser=allUsers[(len(allUsers)-1)]
            lastUserid=int((lastUser.split(":"))[0])+1
            user=str(lastUserid)+":"
            user+=":".join(ls)+"\n"
            usersFile.write(user)
            usersFile.close()
   except Exception as e:
     with open("users.txt",'w') as newusersFile:
            user="1:"
            user+=":".join(ls)+"\n"
            newusersFile.write(user)
            newusersFile.close()  
                
   
       
       
     
       
        
    
    
    
def register():
    ls=[]
    while True:
        firstname=input("please enter your FirstName: ")
        if firstname.isalpha():
           ls.append(firstname)
           break
        else:
           print('---Not Valid----')
           
    while True:
            lastname=input("please enter your lastName: ")
            if lastname.isalpha():
               ls.append(lastname)
               break
            else:
              print('---Not Valid----')
              
    while True:
            email=input("please enter your email: ")
            if (re.fullmatch(regex,email)):
                if getCheckUserEmail(email):   
                  ls.append(email)
                  break
                else:
                     print('---Email Already Exists----')  
            else:
              print('---Not Valid----')
    while True:
            password=input("please enter your password: ")
            if len(password)>=4:
               ls.append(password)
               break
            else:
              print('---password is at least 4 characters ----')      
    while True:
            confirmPassword=input("please confirm your password: ")
            if confirmPassword==password:
               break
            else:
              print('---password needs to be the same as the password ----')
    while True:
            phone=input("please enter the phone: ")
            if (re.fullmatch(phoneregex,phone)) and len(phone)==11:
               ls.append(phone)
               break
            else:
              print('---phone isnot valid ----')                                             
    insertintoFile(ls)
    print(f'*****YOU WILL BE DIRECTED TO LOGIN PAGE****')    
    return login.login()
           