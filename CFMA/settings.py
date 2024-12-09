import os
file_suffix = {
        "exe":  ">+",
        "lnk": "-+",
        "ini": "}>",
        "txt": ">:",
        "a": "<",
        "py": "Python -> ",
        "android": "Android -> "
}


root_path = r"C:\\Users"

#getting default desktop location..
get_user = os.getlogin()
default_path = root_path+"\\"+get_user+"\\OneDrive\\Desktop"
favourites = os.path.dirname(__file__)+"\\Favourites.txt"
##


