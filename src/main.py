import colorama
from colorama import Fore
colorama.init()

# Welcome Text
print(Fore.RED + "Welcome to YYOS!\n" + 
      "\n" + "\    /  \    /   ||    ||||\n" + 
      " \  /    \  /   |  |  |    \n" + 
      "  \/      \/   |    |  |||| \n" + 
      "   |       |    |  |      ||\n" + 
      "   |       |     ||   ||||| \n" + Fore.RESET + 
      Fore.LIGHTMAGENTA_EX + "\nThis is actually just a little thing to learn python with!\n" + 
      "I will be making some improvements with this.\n" + 
      "If you want to know how to use this type in '!HELP'.\n" + 
      "Please do not look at the code, i am very bad lol.\n")
exec(open('prompt.py').read())