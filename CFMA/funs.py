from libpasteurize.fixes.fix_imports import multiple_name_import_match

import settings
import os

##USER COMMANDS
class Folder:
    def __init__(self,name="Folder",path = "",parent = None,contents = None):
        self.name = name
        self.path = path
        self.parent = parent
        self.contents = contents

    def initContents(self,depth):
        FC = os.listdir(self.path) #FC = Folder Contents
        for Item in FC:
            myPath = f'{self.path}\\{Item}'
            if Handler.MultiTool("checkType",Item) == "File":
                myName = Handler.MultiTool("getName",Item)
                newItem = File(myName,myPath,self)
            else:
                myName = Handler.MultiTool("getName", Item)
                if depth < 3:
                    newItem = Folder(myName,myPath,self,Folder.initContents(self,depth+1))
                else:
                    newItem = Folder(myName, myPath, self)
            if self.contents is None:
                self.contents = [newItem]


class File:
    def __init__(self,name = "New",path = "",parent = None):
        self.name = name
        self.parent = parent
        self.path = path

class Commands:
    cmds = {

    }
class Handler:
    def MultiTool(action:str,obj:str):
        action = action.lower()
        fString = obj.split(".")

        if action == "checkType":
            if len(fString) > 1:
                return "File"
            return "Folder"

        elif action == "getName":
            return fString[0]

        elif action == "getExtension":
            return fString[1]

def c_back():
    print("\n>>>Went Back!")
    #update_fold(fold["my_path"].strip("\\"+getFoldName(fold["my_path"])))
    set_fold(os.path.dirname(folder["path"]))
def c_root():
    print("\n>>>Back to Root!")
    set_fold(RootPath)
    
def c_move():
    obj= getDirMatch(input("\n>>>Give Object to move: "),False)
    dest= input(">>>Give Destination: ")
    print("\n>>>Moved "+obj)
    shutil.move(obj, dest) 

def c_delete():
    obj=getDirMatch(input("\n>>>Give Object to Delete: "),False)
    os.remove(obj)
    
def c_favourite():
    obj=getDirMatch(input("\n>>>Give Object to Favourite: "),False)
    work_f = open(Favourites,"a")
    work_f.write(obj+"\n")
    work_f.close()
    
def c_fav_open():
    obj=input("\n>>>Give Object to Open from Favourites: ")
    work_f = open(Favourites,"r")
    for text in work_f:
        reformatted = text.strip("\n")
        if reformatted == obj:
            reformatted = text.split(".")
            if len(reformatted) > 1: ## IS A FILE
                    print("+Openning File: "+text.strip("\n"))
                    os.startfile(text.strip("\n"))
            else: ## IS A FOLDER
                    print("+Openning Folder: "+text.strip("\n"))
                    set_fold(text.strip("\n"))
            return
    work_f.close()
def c_fav_list():
    work_f = open(Favourites,"r")
    unified_string = ""
    for text in work_f:
        unified_string = unified_string+text+"\n"
    print("\n[---{Favourites}---]\n")
    print(unified_string)
    print("\n[---[{}{}{}]---]\n")
FileSuffix = settings.file_suffix
RootPath = settings.root_path
Favourites = settings.favourites

folder = {
    "name": "Desktop",
    "path": settings.default_path,
    "contents": []
}


cmd = {
        "%back":  c_back,
        "%root": c_root,
        "%move": c_move,
        "%delete": c_delete,
        "%fav": c_favourite,
        "%fav_open": c_fav_open,
        "%fav_list": c_fav_list
        
}
c_keyletters = {
        "*":  folder["path"]
}
cmd_kls = c_keyletters
def MAIN():
    get_user = os.getlogin()
    root_path = r"C:\\Users"
    root_path = root_path + "\\" + get_user + "\\OneDrive\\Desktop"
    Root = Folder("Root",root_path)


def kwt(word):
    if len(word) == 1:
        return cmd_keyletters[word]
    else:
        return cmd_keyletters[word[0]]
    return word


    #GET DIR NAME
def getFoldName(the_path):
    my_string = os.path.dirname(the_path)
    return my_string


    #INPUT CHECKING & HANDLING FOR COMMANDS
def inputter():
    my_input = input(">>>Select File/Execute Command: ")
    if my_input.find("%") != 0:
        getDirMatch(my_input,True)
    else:
        cmd[my_input]()
        
    inputter()

def set_fold(path):
    folder["name"] = getFoldName(path)
    folder["path"] = path
    folder["contents"] = os. listdir(path)
    unfold()
    
    inputter()
    
    #UPDATE DIR INFORMATION
def update_fold(path):
    folder["name"] = getFoldName(path)
    folder["path"] = folder["path"]+path
    folder["contents"] = os. listdir(folder["path"])
    unfold()
    
    inputter()

    
    #PRINT CONTENT
def unfold():
    print("\n[---{"+folder["name"]+"}---]\n")
    unified_string = ""
    for item in folder["contents"]:
        reformatted = item.split(".")
        if len(reformatted) > 1: ## IS A FILE
            suffix = reformatted[1]
            if suffix in FileSuffix:
                unified_string = unified_string+(FileSuffix[suffix]+item)
            else:
                unified_string = unified_string+("?> "+item)
        else: ## IS A FOLDER
                unified_string = unified_string+("+"+item)
        unified_string = unified_string+"\n"
        
    print(unified_string)
    print("\n(><) Current Directory: "+folder["path"])
    print("\n[---[{}{}{}]---]\n")
    
def updateFav():
    work_f = open(Favourites,"r")
    ta = []
    for text in work_f:
        reformatted = text.strip("\n")
        ta.append(reformatted)
    FavouriteList = ta
        
    #CHECK DIR CONTENT MATCH
def getDirMatch(match,select):
    for item in folder["contents"]:
        reformatted = item.split(".")
        reformatted_word = reformatted[0]
        
        if reformatted_word.lower() == match.lower(): ##CHECK MATCH
            #CHECK OBJECT TYPE
            x = folder["path"]+"\\"+item
            if select:
                if len(reformatted) > 1: ## IS A FILE
                    print("+Openning File: "+x)
                    os.startfile(x)
                else: ## IS A FOLDER
                    print("+Openning Folder: "+item)
                    set_fold(x)
                return
            else:
                return x
    print(">>>no match found,retry")
    inputter()

if __file__ == "__main__":
    print("hi")