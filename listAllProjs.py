
import projectsMenu 
def listAllProjects(id):
    try:
        with open("projects.txt",'r') as projectFile:
               allprojects=projectFile.readlines()
               if len(allprojects)>0:
                   print("==========================================================================")
                   print("Title\tDetails\tTarget\tStartDate\tEndDate")
                   print("==========================================================================")
                   for l in allprojects:
                      project= l.split(":")
                      print(f'{project[1]}\t{project[2]}\t{project[3]}\t{project[4]}\t{project[5]}')
                   print("==========================================================================")
               else:
                    print("----no projects to be shown----------")       
    except Exception as e:
        print("no projects to be shown")
    return projectsMenu.showProjMenu(id)
##################################