from datetime import date  #today(),
import os  #mkdir()
from shutil import copyfile  #copyfile(source,target)

target_folder='source'
file_name_to_save_to='cpp'
file_extension='.cpp'
module_for_file_making='files.py'

    
def getNewFolder(ushtrimi_i_dates):
    #create new folder
    for i in range(1,20):
        try:
            os.mkdir(ushtrimi_i_dates)
            break
        except FileExistsError:
            ushtrimi_i_dates = ushtrimi_i_dates + ' ('+str(i)+')'
    return ushtrimi_i_dates

def genericCppFile(ushtrimi_i_dates):
    #open/create file and add basic c++ code
    f = open(ushtrimi_i_dates + ".cpp","a+")
    f.write("#include <iostream>")
    f.write("\n\nint main(){\n\n\n\n")
    f.write(r'std::cout<<"\n\n";')
    f.write('\nsystem("pause");')
    f.write("\nreturn 0;")
    f.write("\n}")
    f.close()

def getFormatedDateDMY(delimiter='.'):
    #format date to remove leading 0 from day and month
    today = date.today()
    fdata = today.strftime('%d')
    fmuaji = today.strftime('%m')
    viti = today.strftime('%Y')
    if (fdata[0] == '0'):
        fdata = fdata.replace('0' ,'')
    if (fmuaji[0] == '0'):
        fmuaji = fmuaji.replace('0', '')
    return fdata + delimiter + fmuaji + delimiter + viti


data = getFormatedDateDMY()
data = getNewFolder(data)

saverFilePath=os.getcwd()+'\\'+module_for_file_making

os.chdir(data)
genericCppFile(data)

copyfile(saverFilePath,module_for_file_making)
os.mkdir(target_folder)

