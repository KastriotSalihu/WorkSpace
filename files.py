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
            workingDirectory = workingDirectory + '\\' + target_folder
            break
        except FileNotFoundError:
            print("No '"+target_folder+"' dircetory.")
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
            newfile = file_name_to_save_to+str(i)+file_extension
        except FileNotFoundError:
            f = open(newfile,'w')
            f.close()
            break
    return newfile

def getNewFilePath(workingDirectory):
    #returns full path to file-to-save-to
    workingDirectory = changeToSourceFolder(workingDirectory)
    newfile = file_name_to_save_to + file_extension
    newfile = getNewFileName(newfile)    
    return str(workingDirectory) + '\\' + newfile

def makeSourceFolder(target_folder):
    #create 'source' folder
    try:
        os.mkdir(target_folder)
    except FileExistsError:
        print("Folder '"+target_folder+"' already exists!")
        
def getNewTargetFolder(target_folder):
    #Prompt for a different target folder
    change_target_folder =input("would you like to specify a target folder?(y/n) ")
    if(change_target_folder=='y'):
        target_folder = input("Type target folder name: ")

def saveContentToFile(base_file, target_file):
    workingDirectory=os.getcwd()
    save = input("Would you like to save? (y / n)")
    if (save == 'y'):)
        target = getNewFilePath(workingDirectory)
        copyfile(base_file,target)

basename=getOriginalFileNameAndPath(os.getcwd())
changeToSourceFolder(os.getcwd())
file_name_to_save_to=getNewFileName(file_name_to_save_to)
file_name_to_save_to_path=getNewFilePath(os.getcwd())
getNewTargetFolder(target_folder)
makeSourceFolder(target_folder)
saveContentToFile()


