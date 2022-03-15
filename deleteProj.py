import projectsMenu
def getCheckProjectTitle(title):
       try:
            with open("projects.txt",'r') as projectFile:
                  allprojects=projectFile.readlines()
                  for l in allprojects:
                        if l.split(":")[1]==title:
                           projectFile.seek(0)   
                           projectFile.close()  
                           return False
                  projectFile.close()      
            return True
       except Exception as e:
               return True

#################################

def replaceProjects(ls,id):
    try:
        with open("projects.txt",'w') as projectFile:
               for l in ls:
                   projectFile.write(l) 
               projectFile.close()
               return projectsMenu.showProjMenu(id)
    except Exception as e:
        print("something wrong happenned")                  
##################################
def deleteProject(userid):
    while True:
        title=input("please enter the title of the proj you want to delete or 0 to get back : ")
        if title=="0":
             return projectsMenu.showProjMenu(userid)          
        if getCheckProjectTitle(title):
            print("---wrong project title----")
            continue  
        try:
            with open("projects.txt",'r+') as projectFile:
                allprojects=projectFile.readlines()
                projectFile.close()                           
                for l in allprojects: 
                        project= l.split(":")
                        if project[1]==title:
                            if userid==project[0]:
                                allprojects.remove(l)
                                print(f"****project {title} removed successfully****")
                                replaceProjects(allprojects,userid)
                                return projectsMenu.showProjMenu(userid)
                            else:
                                print(f"----project {title} is not one of your own cant be deleted----")   
                            
        except Exception as e:
            print("----it doesnt exist----")                         
##################################