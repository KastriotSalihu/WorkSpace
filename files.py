from datetime import date  #today(),
import os  #mkdir()
from shutil import copyfile  #copyfile(source,target)

target_folder='source'
file_name_to_save_to='cpp'
file_extension='.cpp'
module_for_file_making='files.py'


def getOriginalFileNameAndPath(workingDirectory):
    #returns full path to file for workspace, based on the folder name
    file_name = os.path.basename(workingDirectory)
    return workingDirectory+'\\'+ file_name + file_extension


def changeToSourceFolder(workingDirectory, target_folder=target_folder):
    #change directory to a target folder, such as 'source'
    os.chdir(workingDirectory)
    while True:
        try:
            os.chdir(target_folder)
            workingDirectory = f'{workingDirectory}\\{target_folder}'
            break
        except FileNotFoundError:
            print(f"No '{target_folder}' dircetory.")
            break
    return workingDirectory

def getNewFileName(newfile):
    #generates numbered name of the file to save to
    for i in range(1,20):
        try:
            f = open(newfile,'r')
            f.close()
            if (i==20):
                print("Limit reached!")
            newfile = f'{file_name_to_save_to}{i}{file_extension}'
        except FileNotFoundError:
            f = open(newfile,'w')
            f.close()
            break
    return newfile

def getNewFilePath(workingDirectory):
    #returns full path to file-to-save-to
    workingDirectory = changeToSourceFolder(workingDirectory)
    newfile = f'{file_name_to_save_to}{file_extension}'
    newfile = getNewFileName(newfile)    
    return str(workingDirectory) + '\\' + newfile

def compileCpp(basename):
    CMDcommand = f'g++ "{basename}" || cmd /k'
    os.system(str(CMDcommand))

def saveContentToFile(base_file):
    save = input("Would you like to save? (y / n)")
    if (save == 'y'):
        target_file=getNewFilePath(os.getcwd())
        copyfile(base_file,target_file)



basename=getOriginalFileNameAndPath(os.getcwd())
compileCpp(basename)
saveContentToFile(basename)


