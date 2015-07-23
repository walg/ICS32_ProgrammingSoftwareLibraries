'''
Ford Tang 46564602
Don Carmona 55162432
ICS 32 Winter 2014
Project #1: Begin the Begin
'''

import os
import glob
import shutil

def askPath() -> str:
    ''' This function ask the user for the root path and returns the given input.
    '''
    exist = False
    path = ''
    while exist == False:
        path = os.path.normpath(str.strip(input('Please input the directory to search:\n')))
        if os.path.isdir(path):
            exist = True
        else:
            print("Directory does not exist, please input another.\n")
    return path

def search_by_name(path:str, filename:str) -> [str]:
    ''' This function searches for the filename and returns a list of where those files are.
    '''
    result = []
    directory_items = os.listdir(path)
    directories = []
    print("Current directory:  " + path)
    
    if os.path.isfile(path + os.sep + filename):
        result.append(path + os.sep + filename)
    
    for item in directory_items:
        try:
            if os.path.isdir(path + os.sep + item):
                directories.append(path + os.sep + item)
        except:
            pass

    for directory in directories:
        result.extend(search_by_name(directory,filename))

    return result

def search_by_name_ending(path:str, extension:str) -> [str]:
    ''' This function searches for the extension and returns a list of files
        that match the extension
    '''
    result = []
    directory_items = os.listdir(path)
    directories = []

    print("Current directory:  " + path)

    result.extend(glob.glob(path + os.sep + "*" + extension))

    for item in directory_items:
        try:
            if os.path.isdir(path + os.sep + item):
                directories.append(path + os.sep + item)
        except:
            pass

    for directory in directories:
        result.extend(search_by_name_ending(directory, extension))

    return result

def search_by_size(path:str, size:int) -> [str]:
    '''This function searches for files larger than the specified size and will return
         the result in a list
         '''
    result = []
    directory_items = os.listdir(path)
    directories = []
    files = []

    print("Current directory:  " + path)

    for item in directory_items:
        if os.path.isfile(path + os.sep + item):
            files.append(path + os.sep + item)

    for file in files:
        if os.stat(file).st_size >= size:
            result.append(file)

    for item in directory_items:
        try:
            if os.path.isdir(path + os.sep + item):
                directories.append(path + os.sep + item)
        except:
            pass

    for directory in directories:
        result.extend(search_by_size(directory, size))

    return result

def print_path_only(fileList:[str]) -> None:
    ''' Function prints out the directories from the list of files
    '''
    print("Printing path(s):")
    for file in fileList:
        print(os.path.dirname(file))
    print()

    return None

def print_first_line_of_text(fileList:[str]) -> None:
    '''Function prints out the first line from each file in the list
    '''
    print('Printing First Line of File(s):')
    for file in fileList:
        print("First line of " + file)
        print(open(file).readline())
    print()

    return None

def copy_file(fileList: [str]) -> None:
    '''Function creates duplicate files of the files in the list with the
    extension .dup added to it
    '''
    print('Copying File(s):')
    for file in fileList:
        print ("Creating " + file + ".dup")
        shutil.copyfile(file, file + ".dup")
    print()
    
    return None

def touch_file(fileList:[str]) -> None:
    '''Function modifies the files' last timestamp to be the current time
    '''
    print('Touching File(s)')
    for file in fileList:
        print("modifying " + file)
        os.utime(file)
    print()
    
    return None

def menu() -> None:
    ''' This function is the main menu for the program and will ask the user for inputs on how and what to process
    '''
    filelist = []
    path = askPath()
    valid_choice = False
    while valid_choice == False:
        choice = str.strip(input('**************************************************\nSearch by Name? (type N)\nSearch by Extension or Name Ending in? (type E)\nSearch by Size? (type S)\n**************************************************\nHow would you like to search?:  ')).upper()
        if choice == 'N' or choice == 'E' or choice == 'S':
            print()
            valid_choice = True
        else:
            print ('\nInvalid selection, please try again.\n')
            
    if choice == 'N':
        name = None
        while True:
            name = str.strip(input('What file name would you like to search for?  '))
            if name != '':
                filelist = search_by_name(path, name)
                print()
                break
            else:
                print('\nEmpty input does not work, please try again.\n')
                
    elif choice == 'E':
        extension = None
        while True:
            extension = str.strip(input('What extension would you like to search for?  '))
            if extension != '':
                filelist = search_by_name_ending(path, extension)
                print()
                break
            else:
                print('\nEmpty input does not work, please try again.\n')
                
    else:
        size = 0
        while True:
            try:
                size = int(str.strip(input('What is the minimum size that you would like to search for (in bytes)?  ')))
                filelist = search_by_size(path, size)
                print()
                break
            except:
                print('\nInvalid input, please try again.\n')
                
    valid_action = False
    while valid_action == False:
        action = str.strip(input('**************************************************\nPrint path only? (type P)\nPrint first line of text? (type L)\nCopy file? (type C)\nTouch file? (type T)\n**************************************************\nWhat would you like to do?:  ')).upper()
        if action == 'P' or action == 'L' or action == 'C' or action == 'T':
            print()
            valid_action = True
        else:
            print ('\nInvalid selection, please try again.\n')
    if action == 'P':
        print_path_only(filelist)
    elif action == 'L':
        print_first_line_of_text(filelist)
    elif action== 'C':
        copy_file(filelist)
    else:
        touch_file(filelist)
    choice = None
    while True:
        choice = str.strip(input('Would you like to search again? (Y for yes, N for No):  ')).upper()
        if choice == 'Y':
            print('\nRestarting Search Program.\n')
            break
        elif choice == 'N':
            print('\nGood-bye!\n')
            break
    if choice == 'Y':
        menu()
    
if __name__ == '__main__':
    menu()
