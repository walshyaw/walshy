# ALEX WALSH
# Created on 01/13/2025. Last modified on 01/13/2025.
# https://github.com/walshyaw/

from colorama import Fore

def main():
    init_calc()

def init_calc():
    RED = Fore.RED
    GREEN = Fore.GREEN
    RESET = Fore.RESET
    total = 0
    skip = 0
    is_running = True
    options = ["A", "S", "M", "D", "C", "E"]

    while is_running:
        print(f"""{GREEN}
 _____       _            _       _             
/  __ \     | |          | |     | |            
| /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
 \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
{RESET}""")

        print(f"{"TOTAL:":>22} {GREEN}{total:.3f}{RESET}")

        # GRABS FIRST CALCULATOR INPUT, IS SKIPPED FOR THE REST OF THE PROGRAM AS IT USES A RUNNING TOTAL.
        while skip == 0:
            try:
                num = float(input("\nEnter a num: "))
                total += num
                skip += 1
                break
            except ValueError:
                print("ERROR! NUMBER MUST BE VALID.")
        
        # GRABS OEPRATOR CHOICE
        choice = input("\n(A)dd, (S)ubtract, (M)ultiply, (D)ivide, (C)lear, (E)xit: ")
        while choice not in options:
                choice = input("(A)dd, (S)ubtract, (M)ultiply, (D)ivide, (C)lear, (E)xit: ")
        print()
        
        # GRABS A SECOND NUMBER
        while is_running and choice != "C" and choice != "E":
            try:
                num = float(input("Enter a num: "))
                break
            except ValueError:
                print("ERROR! NUMBER MUST BE VALID.\n")
        
        # CALLS THE ASSOCIATED FUNCTIONS.
        match choice:
            case "A":
                total = add(total, num)
            case "S":
                total = sub(total, num)
            case "M":
                total = mult(total, num)
            case "D":
                total = divi(total, num)
            case "C":
                total = 0
                skip = 0
            case "E":
                print(f"""{RED}
                      ---------------------------------------------------

 ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░              
 ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░ 
                      
                       ---------------------------------------------------                                                                            
                                                                                                   {RESET}""")
                is_running = False

def add(total, num):
    return total + num

def sub(total, num):
    return total - num

def mult(total, num):
    return total * num

def divi(total, num):
    return total / num

if __name__ == "__main__":
    main()