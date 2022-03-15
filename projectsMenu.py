from Edit import editProj
import createProj 
import deleteProj
import listAllProjs
import search
import login
import Edit
                       
##################################
def showProjMenu(id):
    print(f"the id is {id}")
    while True:
        print("**************Hello Sir Check the Menu********")
        print("1)Create project \t 2)Edit A project \t 3)View All projects \t 4)Delete A project \t 5)Search for a project 6)back")
        inp=input("Enter Your Choice Number: ")
        match inp:
            case "1":
                return createProj.createproj(id)
            case "2":
                return Edit.editProj(id)
            case "3":
                return listAllProjs.listAllProjects(id)
            case "4":
                return deleteProj.deleteProject(id)                
            case "5":
                return search.search(id)
            case "6":
                return login.login()            

