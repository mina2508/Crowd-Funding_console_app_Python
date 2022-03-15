import projectsMenu
def getinfo(propIndex,val):
    try:
        with open("projects.txt",'r') as projectFile:
               allprojects=projectFile.readlines()
               counter=0
               if len(allprojects)>0:
                   print("==========================================================================")
                   print("Title\tDetails\tTarget\tStartDate\tEndDate")
                   print("==========================================================================")
                   for l in allprojects:
                      project= l.split(":")
                      if project[propIndex]==val:
                         print(f'{project[1]}\t{project[2]}\t{project[3]}\t{project[4]}\t{project[5]}')
                         counter+=1
                   if counter==0:
                          print("=========================No Prop with these values========================")   
                   print("==========================================================================")
               else:
                    print("----no projects to be shown----------")       
    except Exception as e:
        print("no projects to be shown")
    

def search(userid):
   print("*********Search with any property but the date*********")
   while True: 
       
     inp=input("please enter the property you want to search with or 0 to get back : " )
     match inp.lower():
            case "title":
                title=input("please enter the title value:  ")
                getinfo(1,title)
                continue
            case "details":
                details=input("please enter the details value:  ")
                getinfo(2,details)
                continue                 
            case "target":
                target=input("please enter the target value:  ")
                getinfo(3,target)
                continue 
            case "0":
                 return projectsMenu.showProjMenu(userid)

                     
                 
     print("---Not Valid column---")
