import getpass
import os
import datetime
import traceback
import sys
import subprocess

import colorama
from colorama import Fore, Back, Style
colorama.init()

def commandLine(command):
         
    #closes the cmd
    if command == '!EXIT' or command == '!E':
        print('\nExiting...')
        exit()
    
    #restarts the program
    elif command == '!RESTART' or command == '!R':
        print('\nRestarting...\n')
        exec(open('Main.py').read())
        
    #help command
    elif command == '!HELP' or command == '!H':
         print('\nHere the commands you can use:\n' + 
              '"!EXIT" Or "!E" = "Exits the OS"\n' + 
              '"!HELP" Or "!H" = "Gives you info on what you can do"\n' + 
              '"!PATH" Or "!P" = "Shows the directory you are in"\n' + 
              '"!LIST" Or "!L" = "Shows a list of files in the directory you are in"\n' + 
              '"!TEXT" Or "!T" = "Reads a text file"\n' + 
              '"!CD" = "Go to a directory"\n')
    
    #opens up the code prompt
    elif command == '!CODE' or command == '!C':
            codePrompt()
        
    #shows the path you are in
    elif command == '!PATH' or command == '!P':
        print('\n' + os.getcwd() + '\n')
        
    #shows list of .py files in the directory
    elif command == '!LIST' or command == '!L':
        print('\n' + '\n'.join(os.listdir()) + '\n')
         
    #reads a txt file
    elif command == '!TEXT' or command == '!T':
        file_name = input("\nEnter the path of the text file: ")
        with open(file_name, 'r') as file:
            print('\n')
            content = file.read()
            print(content)
        
    #go to a directory
    elif command.startswith('!CD'):
        path = command.split(' ', 1)
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f'Directory "{path}" not found.')
            
    else:
        print(f'\nInvalid command: {command}\n')

#terminal
def terminal():
    print('Type a command:\n')
    while True:
        try:
            command = input('[< ')
            commandLine(command)
        except Exception as e:
            print(f'\nAn error occurred: {e}')
            print('Saving error to crash log...\n')
            save_error_log(str(e))
            
def codeLine(prompt):
    if prompt == 'YY "restart"':
        print(Fore.RESET)
        print('\nRestarting...\n')
        exec(open('Main.py').read())
        
    elif prompt == 'YY "intro"':
        print('\n   Hello, welcome to YYOS!\n')
    
    elif prompt == 'YY "version"':
        file_name = 'version.txt'
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)

# do this thing later
    elif prompt == 'YY "help"':
         print('\n   Here is a list that shows what you can do!:\n' + 
              '\n' + 
              '\n' + 
              '\n' + 
              '\n' + 
              '\n' + 
              '\n')
        
    else:
        print(f'\n   Invalid command: {prompt}\n')
            
def codePrompt():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '\n   Type in some code:\n')
    while True:
        try:
            prompt = input('   < ')
            codeLine(prompt)
        except Exception as e:
            print(f'\nAn error occurred: {e}')
            print('Saving error to crash log...\n')
            save_error_log(str(e))
        
def save_error_log(error_message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder_name = 'crash'
    file_name = f'crash_{timestamp}.txt'
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, file_name)

    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = traceback.extract_tb(exc_traceback)
    
    filePath = os.path.abspath(__file__)
    fileName = os.path.basename(file_path)

    with open(file_path, 'w') as file:
        file.write(f'Error: {error_message}\n\n')
        file.write('Traceback:\n')
        for traceback_line in traceback_details:
            file.write(f"File 'Prompt.py', line {traceback_line.lineno}, in {traceback_line.name}\n")
            file.write(f'    {traceback_line.line}\n')
            file.write('Make sure to report this bug on: https://github.com/YY0100/YYOS')
        file.write('\n')

if __name__ == '__main__':
    terminal()