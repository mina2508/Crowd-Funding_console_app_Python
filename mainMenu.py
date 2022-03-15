
import register  
import login 
def mainFunc():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t\t \t Crowd Funding  \t\t")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    while True:
        choice=input("please enter L to login or R to register: ")
        if choice.lower()=='l':
           return login.login()
        elif choice.lower()=="r":
           return register.register()
        else:
            print("------please enter valid choice------")    

mainFunc()        