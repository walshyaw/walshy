# ALEX WALSH
# Created on 12/30/2024. Last modified on 12/30/2024.
# https://github.com/walshyaw/

from colorama import Fore

# DEFINES THE BALANCE AND INITALIZES THE BANK.
def main():
    bal = 0
    init_bank(bal)

# INITALIZES THE BANK AND DISPLAYS THE POSSIBLE FUNCTIONS THAT CAN BE RAN WITHIN IT.
def init_bank(bal):

    is_running = True

    while is_running:
        print(f"""\n{GREEN}
         __,--,_.   .______        ___      .__   __.  __  ___         __,--,_.
        /       |   |   _  \\      /   \\     |  \\ |  | |  |/  /        /       |
       |   (----`   |  |_)  |    /  ^  \\    |   \\|  | |  '  /        |   (----`
        \\   \\       |   _  <    /  /_\\  \\   |  . `  | |    <          \\   \\    
    .----)   |      |  |_)  |  /  _____  \\  |  |\\   | |  .  \\     .----)   |   
    |_    __/       |______/  /__/     \\__\\ |__| \\__| |__|\\__\\    |_    __/    
      '--'                                                          '--'       
              
    BY: ALEX WALSH\n{RESET}""")

        
        print(f"\n1. Show Balance")
        print(f"2. Deposit")
        print(f"3. Withdraw")
        print(f"4. Exit")

        # INPUT VALIDATION
        while True:

            request = input("\n[1, 2, 3, 4]: ")

            try:
                request = int(request)
                if request not in (1, 2, 3, 4):
                    print(f"{RED}Invalid Response.{RESET} Response must be 1, 2, 3, or 4")
                else:
                    break
            except ValueError:
                print(f"{RED}Invalid Response.{RESET} Response must be 1, 2, 3, or 4")
        #

        match request:
            case 1:

                get_bal(bal)

            case 2:

                bal = deposit(bal)
            
            case 3:

                bal = withdraw(bal)

            case _:
                is_running = False
                print(f"\n{GREEN} GOODBYE! {RESET}\n")

# ALLOWS FOR DEPOSITS TO THE BALANCE AND THEN RETURNS IT.
def deposit(bal):
    
    depo = input(f"\nEnter the amount you wish to deposit: {GREEN}+${RESET}")
    
    # INPUT VALIDATION
    while True:
        try:
            depo = float(depo)
            break
        except ValueError:
            depo = input(f"{RED}Invalid Response.{RESET} Response must be numeric: $")
    #
    
    bal += depo

    print(f"\nYou have deposited {GREEN}${depo:.2f}{RESET} into your account.")
    input("\nPress any key to continue...")
    return bal

# ALLOWS FOR WITHDRAWS FROM THE BALANCE AND THEN RETURNS IT.
def withdraw(bal):

    # INPUT VALIDATION
    while True:

        withdr = input(f"\nEnter the amount you wish to withdraw: {RED}-${RESET}")

        try:
            withdr = float(withdr)
            if withdr <= bal and withdr >= 0:
                break
            else:
                print(f"{RED}Invalid Response.{RESET} Response must not exceed your overall balance of {GREEN}${bal:.2f}{RESET} and may not be a negative value.")

        except ValueError:
            print(f"{RED}Invalid Response.{RESET} Response must be numeric.")
    #
    
    bal -= withdr

    print(f"\nYou have withdrawn {RED}${withdr:.2f}{RESET} from your account.")
    input("\nPress any key to continue...")
    return bal

# DISPLAYS CURRENT BALANCE.     
def get_bal(bal):
    print(f"\nYour current balance is {GREEN}${bal:.2f}{RESET}.")
    input("\nPress any key to continue...")

if __name__ == '__main__':

    GREEN = Fore.GREEN
    RED = Fore.RED
    RESET = Fore.RESET

    main()