import os
import shutil

import settings
import funs as run

print(settings.file_suffix)
############### ACTION
if settings.get_user == "panik":
    my_type = input("What r u doin ||||||||: ")
    ####Pre-determined
    if my_type.lower() == "work":

        run.update_fold("\\Retarded")
    else:
        run.set_fold(settings.default_path)
else:
    run.set_fold(settings.default_path)

