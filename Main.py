import colorama
from colorama import Fore, Back, Style
colorama.init()

# Welcome Text
print(Fore.RED + Style.BRIGHT + "Welcome to YYOS!\n" + 
      "\n" + "\    /  \    /   ||    ||||\n" + 
      " \  /    \  /   |  |  |    \n" + 
      "  \/      \/   |    |  |||| \n" + 
      "   |       |    |  |      ||\n" + 
      "   |       |     ||   ||||| \n" + Fore.RESET + Back.RESET + 
      Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\nThis is actually just a little thing to learn python with!\n" + 
      "I will be making some improvements with this.\n" + 
      "If you want to know how to use this type in '!HELP'.\n" + 
      "Please do not look at the code, i am very bad lol.\n")
exec(open('Prompt.py').read())