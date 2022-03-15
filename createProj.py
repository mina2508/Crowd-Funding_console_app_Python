import projectsMenu 
import datetime
def getStartDate(id):  
  while True:
   try:   
     date_entry = input('Enter start date in YYYY-MM-DD format or 0 to getback: ')
     if date_entry=="0":
          return projectsMenu.showProjMenu(id) 
     else:       
        year, month, day = map(int, date_entry.split('-'))
        Startdate = datetime.date(year, month, day)
        if datetime.date.today()>Startdate:
            print("---the start date cant be before today----")
        else:      
          return Startdate
   except Exception as e:
       print("not valid date")
####################################################
def getEndDate(startdate,id):
  while True:
   try:   
     date_entry = input('Enter The end date in YYYY-MM-DD format or 0 to get back: ')
     if date_entry=="0":
          return projectsMenu.showProjMenu(id) 
     else:          
        year, month, day = map(int, date_entry.split('-'))
        endDate = datetime.date(year, month, day)
        if startdate>=endDate:
            print("-------the end date cant be before the start date--------")
        else:      
          return endDate
   except Exception as e:
       print("--------not valid date------") 
####################################################3
def insertintoFile(ls):
   try:
        with open("projects.txt",'r+') as projectFile:
                projectFile.readlines()
                proj="\n"+":".join(ls)
                projectFile.write(proj)
                projectFile.close()
   except Exception as e:
        with open("projects.txt",'w') as projectFile:    
                proj=":".join(ls)
                projectFile.write(proj)
                projectFile.close() 
####################################################
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
####################################################              
def createproj(id):
    ls=[]
    ls.append(id)
    while True:
        title=input("please the title of the proj or 0 to get back: ")
        if title=="0":
              return projectsMenu.showProjMenu(id)
        elif title.isalpha():
           if getCheckProjectTitle(title): 
              ls.append(title)
              break
           else:
             print('--- the project already exist----')  
        else:
           print('---Not Valid title----')
           
    while True:
            det=input("please some details about the proj or 0 to getback: ")
            if det=="0":
              return projectsMenu.showProjMenu(id)            
            elif det.isdigit():
               print('---Not Valid----')
            elif len(det)==0 or det=="\n":
                print('---Not Valid----')  
            else:
              ls.append(det)
              break
              
    while True:
            target=input("please enter total target or 0 to get back: ")
            if target=="0":
                  return projectsMenu.showProjMenu(id)                
            elif target.isdigit():
               ls.append(target)
               break
            else:
              print('---Not Valid ----')      
    startdate=getStartDate(id)
    enddate=getEndDate(startdate,id)
    startdate=startdate.strftime('%Y/%m/%d')
    enddate=enddate.strftime('%Y/%m/%d')
    ls.append(startdate) 
    ls.append(enddate)        
    insertintoFile(ls)
    print("****project created successfully****")
    return projectsMenu.showProjMenu(id)
