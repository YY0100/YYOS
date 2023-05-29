import os
import datetime
import traceback
import sys

import colorama
from colorama import Fore
colorama.init()

#felt silly
def restart_thing():
    print(Fore.RESET)
    print('Restarting...\n')
    exec(open('main.py').read())

def commandLine(command):
    #closes the cmd
    if command == '!EXIT' or command == '!E':
        print('\nExiting...')
        exit()
    
    #restarts the program
    elif command == '!RESTART' or command == '!R':
        restart_thing()
    
    #refresh thing
    elif command == '!REFRESH':
        if os.name == 'nt':
            os.system('cls')
            exec(open('main.py').read())
        
    #help command
    elif command == '!HELP' or command == '!H':
         print(Fore.LIGHTYELLOW_EX + '\n Here the commands you can use:\n' + 
              '\n "!EXIT" Or "!E" = "Exits YYOS"\n\n' + 
              ' "!HELP" Or "!H" = "Gives you info on what you can do"\n\n' + 
              ' "!PATH" Or "!P" = "Shows the directory you are in"\n\n' + 
              ' "!LIST" Or "!L" = "Shows a list of files in the directory you are in"\n\n' + 
              ' "!TEXT" Or "!T" = "Reads a text file"\n\n' + 
              ' "!CODE" Or "!C" = "Runs YY CODE"\n\n' + 
              ' "!REFRESH" = "Clears everything"\n\n' + 
              ' "!RESTART" Or "!R" = "Restarts YYOS"\n\n' + 
              ' "!VERSION" Or "!V" = "Shows the version of the program"\n\n' + 
              ' "!CD" = "Go to a directory"\n' + Fore.LIGHTMAGENTA_EX)
    
    #opens up the code prompt
    elif command == '!CODE' or command == '!C':
            codePrompt()
    
    #decided to make it a txt file because why not
    elif command == '!VERSION' or command == '!V':
        file_name = 'version.txt'
        print()
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
        print()
        
    #shows the path you are in
    elif command == '!PATH' or command == '!P':
        print('\n' + os.getcwd() + '\n')
        
    #shows list of .py files in the directory
    elif command == '!LIST' or command == '!L':
        print('\n' + '\n'.join(os.listdir()) + '\n')
         
    #reads a txt file
    elif command == '!TEXT' or command == '!T':
        file_name = input('\nEnter the path of the text file: ')
        file_name = file_name.replace('/', '\\')  # dumb ass shit
        try:
            with open(file_name, 'r') as file:
                print()
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f'\nDirectory not found: {file_name}')
        print()
        
    #go to a directory
    elif command.startswith('!CD'):
        new_dir = input('\nEnter the path of the directory: ')
        try:
            os.chdir(new_dir)
            print(f"\nDirectory changed to {new_dir} successfully!\n")
        except FileNotFoundError:
            print(f"\nDirectory not found: {new_dir}\n")
            
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
            
#hhh i am such a silly willy
def codeLine(prompt):
    if prompt == 'YY "restart_program"':
        restart_thing()
        
    if prompt == 'YY "restart"':
        print(Fore.RESET)
        print('   Restarting...')
        print(Fore.LIGHTCYAN_EX, end='')
        codePrompt()
        
    elif prompt == 'YY "intro"':
        print('\n     Hello, welcome to YY code!\n')

    elif prompt == 'YY "help"':
         print('\n     Here is a list that shows what you can do!:\n' + 
              '\n     YY "restart_program" = restarts the whole program\n' + 
              '     YY "restart" = restarts\n' + 
              '     YY "intro" = does the intro\n')
        
    else:
        print(f'\n     Invalid code: {prompt}\n')
            
def codePrompt():
    print(Fore.LIGHTCYAN_EX + '\n   WELCOME TO YY CODE!')
    print('   Do YY "help" to see what you can do!')
    print('\n   Type in some code:\n')
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
            file.write(f"File 'prompt.py', line {traceback_line.lineno}, in {traceback_line.name}\n")
            file.write(f'    {traceback_line.line}\n')
            file.write('Make sure to report this bug on: https://github.com/YY0100/YYOS')
        file.write('\n')

if __name__ == '__main__':
    terminal()