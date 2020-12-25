import colorama
from colorama import Fore, Style

colorama.init(autoreset = True)

high = 10

print(Style.BRIGHT + Fore.BLACK + Fore.GREEN + "  " + "¡FELIZ NAVIDAD!")
for i in range(high):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
        print(Fore.RED + " " * (high - i - 1) + "*" * (2 * i + 1))
    else:
        print(Fore.GREEN + " " * (high - i - 1) + "*" * (2 * i + 1))

for j in range(int(high/2)):
    print(Fore.MAGENTA + Fore.YELLOW + " " * int(high - high/4) + "*" * int(high/2))
