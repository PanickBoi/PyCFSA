import os
#my_string = r"C:\Users\panik\OneDrive\Desktop\Retarded\Visual Studio Code.lnk"
#os.startfile(my_string)
kws = ["back","root","delete","rewrite","new","move"]

default_path = r"C:\\Users"
#getting default desktop location..
for item in os. listdir(default_path):
    print (item)
get_user = input("Who's your user?: ")
default_path = default_path+"\\"+get_user+"\\OneDrive\\Desktop"
##

fold = {
    "my_name": "Desktop",
    "my_path": default_path,
    "my_contents": []
}

    #GET DIR NAME
def getFoldName(the_path):
    my_string = ""
    for letter in the_path:
        if letter != "\\":
            my_string= my_string+letter
        else:
            my_string= ""
    return my_string


    #INPUT CHECKING & HANDLING
def inputter():
    my_input = input(">>>Select File: ")
    if my_input.find("%") != 0:
        getDirMatch(my_input)
    else:
        if 
    


    #UPDATE DIR INFORMATION
def update_fold(path):
    fold["my_name"] = getFoldName(path)
    fold["my_path"] = path
    fold["my_contents"] = os. listdir(fold["my_path"] )
    unfold()
    
    inputter()

    
    #PRINT CONTENT
def unfold():
    print("[---"+fold["my_name"]+"---]")
    for item in fold["my_contents"]:
        print (">"+item+"\n")

    #CHECK DIR CONTENT MATCH
def getDirMatch(match):
    for item in fold["my_contents"]:
        reformatted = item.split(".")
        reformatted = reformatted[0]
        
        if reformatted.lower() == match.lower():
            if len(reformatted) > 1 and type(reformatted) != type("str"):
                os.startfile(fold["my_path"]+"\\"+item)
            elif len(reformatted) == 0 or type(reformatted) == type("str"):
                update_fold(fold["my_path"]+"\\"+item)
            return
    print("no match found,retry")
    inputter()

############### ACTION

my_type = input("What r u doin ||||||||: ")
####Pre-determined
if my_type.lower() == "work":

    update_fold(fold["my_path"]+"\\Retarded")
    
else:
    
    update_fold(fold["my_path"]+"\\"+my_type)
    
    
