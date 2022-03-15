import createProj
import datetime
import time
import projectsMenu

def replaceProjects(ls,id):
    try:
        with open("projects.txt",'w') as projectFile:
               for l in ls:
                   projectFile.write(l) 
               projectFile.close()
               print("****UPDATTED****")
    except Exception as e:
        print("--------something wrong happenned----------")        


#####################################################
def editProjTitle(title,userid,newtitle):
     try:
            with open("projects.txt",'r') as projectFile:
                allprojects=projectFile.readlines()
                projectFile.close()                           
                for l in allprojects: 
                        project= l.split(":")
                        if project[1]==title:
                            if project[0]==userid:
                                project[1]=newtitle
                                idx=allprojects.index(l)
                                proj=":".join(project)
                                allprojects[idx]=proj
                                replaceProjects(allprojects,userid)                                
                            else:
                                print(f"----project {title} is not one of your own cant be deleted----")                            
     except Exception as e:
            print(f"----it doesnt exist {e}----")  

###############################################
def editProjDetails(title,userid,newdetails):
     try:
            with open("projects.txt",'r') as projectFile:
                allprojects=projectFile.readlines()
                projectFile.close()                           
                for l in allprojects: 
                        project= l.split(":")
                        if project[1]==title:
                            if project[0]==userid:
                                project[2]=newdetails
                                idx=allprojects.index(l)
                                proj=":".join(project)
                                allprojects[idx]=proj
                                replaceProjects(allprojects,userid)                                
                            else:
                                print(f"----project {title} is not one of your own cant be deleted----")                            
     except Exception as e:
            print(f"----it doesnt exist {e}----")  
###############################################
def editProjTarget(title,userid,newtarget):
     try:
            with open("projects.txt",'r') as projectFile:
                allprojects=projectFile.readlines()
                projectFile.close()                           
                for l in allprojects: 
                        project= l.split(":")
                        if project[1]==title:
                            if project[0]==userid:
                                project[3]=newtarget
                                idx=allprojects.index(l)
                                proj=":".join(project)
                                allprojects[idx]=proj
                                replaceProjects(allprojects,userid)                                
                            else:
                                print(f"----project {title} is not one of your own cant be deleted----")                            
     except Exception as e:
            print(f"----it doesnt exist {e}----")
################################################

################################################
      
def checkStartdate(startdate,title,userid):
    while True:
         try:
            with open("projects.txt",'r') as projectFile:
                allprojects=projectFile.readlines()
                projectFile.close() 
                print(userid)                          
                for l in allprojects:
                        project= l.split(":")                        
                        if project[1]==title:
                            if project[0]==userid:
                               enddate=project[5].rstrip("\n")
                               end = datetime.datetime.strptime(enddate, '%Y/%m/%d')
                               if end>startdate :
                                    startdate=startdate.strftime('%Y/%m/%d') 
                                    project[4]=startdate
                                    print(project[1])
                                    idx=allprojects.index(l)
                                    proj=":".join(project)
                                    allprojects[idx]=proj
                                    replaceProjects(allprojects,userid)
                                    return True  
                               else:
                                   print(f"---- cant insert start date after the end date {enddate}---- ")
                                   return False                              
                            else:
                                print(f"----project {title} is not one of your own cant be deleted----") 
                                return False                           
         except Exception as e:
            print(f"----it doesnt exist {e}----")
            return False  
###############################################
def editProjStart(title,userid):
  while True:
    try:   
      date_entry = input('Enter a date in YYYY-MM-DD format or 0 to getbback: ')
      if date_entry=="0":
            return projectsMenu.showProjMenu(userid)          
      year, month, day = map(int, date_entry.split('-'))
      Startdate = datetime.datetime(year, month, day)
      if datetime.datetime.today()>Startdate: 
        print("---the start date cant be before today----")   
      else:
         
        if checkStartdate(Startdate,title,userid):        
          return Startdate
    except Exception as e:
      print("not valid date")                            
################################################     
def checkEnddate(enddate,title,userid):
    while True:
         try:
            with open("projects.txt",'r') as projectFile:
                allprojects=projectFile.readlines()
                projectFile.close()                           
                for l in allprojects:
                        project= l.split(":")
                        
                        if project[1]==title:
                            if project[0]==userid:
                               startdate=project[4]
                               start = datetime.datetime.strptime(startdate, '%Y/%m/%d')
                               if enddate>start :
                                    enddate=enddate.strftime('%Y/%m/%d') 
                                    project[5]=enddate
                                    idx=allprojects.index(l)
                                    proj=":".join(project)
                                    allprojects[idx]=proj
                                    replaceProjects(allprojects,userid)
                                    return True  
                               else:
                                   print(f"---- cant insert end date before {startdate}---- ")
                                   return False                              
                            else:
                                print(f"----project {title} is not one of your own cant be deleted----") 
                                return False                           
         except Exception as e:
            print(f"----it doesnt exist {e}----")
            return False  
###############################################
def editProjEnd(title,userid):
 while True:
    try:   
      date_entry = input('Enter a End date in YYYY-MM-DD format or 0 to get back: ')
      if date_entry=="0":
             return projectsMenu.showProjMenu(userid) 
      year, month, day = map(int, date_entry.split('-'))
      enddate = datetime.datetime(year, month, day)
      if datetime.datetime.today()>enddate: 
        print("---the end date cant be before today----")   
      else:
         
        if checkEnddate(enddate,title,userid):        
          return enddate
    except Exception as e:
      print("not valid date")                            
################################################
def editProj(userid):
    while True:
        title=input("enter the title of the project you would like to update or 0 to get back: ")
        if title=="0":
          return projectsMenu.showProjMenu(userid)          
        elif createProj.getCheckProjectTitle(title):
          print("--- the title doesnt exist----")    
        else:                
          inp=input("please enter the property you want to update or 0 to get back:  ")
          match inp.lower():
                case "title":
                    newtitle=input("please enter the newtitle or 0 to get back:  ")
                    print(f'============the user id {userid} the title is {title} and newtitle is {newtitle}===========')
                    if newtitle=="0":
                      return projectsMenu.showProjMenu(userid)                 
                    elif newtitle.isalpha():
                        editProjTitle(title,userid,newtitle)
                        continue
                    else:
                        print('---Not Valid title----')   
                    
                case "details":
                    newdetails=input("please enter the new details or 0 to get back:  ")
                    if newdetails=="0":
                        return projectsMenu.showProjMenu(userid)                  
                    elif newdetails.isdigit():
                        print('---Not Valid----')
                    elif len(newdetails)==0 or newdetails=="\n":
                      print('---Not Valid----')  
                    else:                
                        editProjDetails(title,userid,newdetails)
                        continue
                        
                case "target":
                    newtarget=input("please enter the new target or 0 to get back:  ")
                    if newtarget=="0":
                        return projectsMenu.showProjMenu(id)                   
                    elif newtarget.isnumeric():
                        editProjTarget(title,userid,newtarget)
                        continue
                        
                    else:
                        print('---Not Valid ----') 
    
                case "start":
                    editProjStart(title,userid)
                    continue
                                
                case "end":
                    editProjEnd(title,userid)
                    continue
                case "0":
                    return projectsMenu.showProjMenu(id)          

                
