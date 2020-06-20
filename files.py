from datetime import date  #today(),
import os  #mkdir()
from shutil import copyfile  #copyfile(source,target)

target_folder='source'
file_name_to_save_to='cpp'
file_extension='.cpp'
module_for_file_making='files.py'
file=f'{file_name_to_save_to}{file_extension}'

def getOriginalFileNameAndPath(workingDirectory):
    #returns full path to file for workspace, based on the folder name
    file_name = os.path.basename(workingDirectory)
    return f'{workingDirectory}\\{file_name}{file_extension}'

def changeToSourceFolder(target_folder=target_folder):
    #change directory to a target folder, such as 'source'
    if(os.path.isdir(f'./{target_folder}')):
        os.chdir(target_folder)
    else:
        print(f"No '{target_folder}' dircetory.")

def getNewFileName(newfile):
    #generates numbered name of the file to save to
    i=1
    while True:
        if(os.path.isfile(f'./{newfile}')):
           newfile=f'{file_name_to_save_to}{i}{file_extension}'
           i=i+1
        else:
            f = open(newfile,'w')
            f.close()
            break
    return newfile

def getNewFilePath():
    #returns full path to file-to-save-to
    changeToSourceFolder()
    newfile = getNewFileName(file)    
    return f'{os.getcwd()}\\{newfile}'

def compileCpp(basename):
    CMDcommand = f'g++ "{basename}" || cmd /k'
    os.system(str(CMDcommand))

def saveContentToFile(base_file):
    save = input("Would you like to save? (y / n)")
    if (save == 'y'):
        target_file=getNewFilePath()
        copyfile(base_file,target_file)



basename=getOriginalFileNameAndPath(os.getcwd())
compileCpp(basename)
saveContentToFile(basename)


