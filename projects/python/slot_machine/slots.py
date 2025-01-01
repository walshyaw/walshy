import random
from colorama import Fore

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

def main():
    bal = 1000
    print_intro()
    init_slotmachine(bal)



def init_slotmachine(bal):
    is_running = True
    bet_amount = 0
    spin = 0
    result = 0
    slots = init_slots()

    print(f"Your starting balance is {GREEN}${bal:.2f}{RESET}.")

    while is_running:
        
        while True:
            try:
                bet_amount = float(input("Enter the amount you would like to bet: $"))
            except ValueError:
                bet_amount = float(input(f"{RED}Invalid Response.{RESET} Response must be a valid numerical value."))
            if bet_amount > bal or bet_amount <= 0:
                print(f"{RED}Invalid Response.{RESET} Response must be higher then zero and must not exceed your current balance of {GREEN}${bal}{RESET}.")
            else:
                break
        
        results = [random.choice(slots), random.choice(slots), random.choice(slots)]

        print("\n*******************")
        print(f"   {results[0]}   {results[1]}   {results[2]}   ")
        print("*******************\n")

        if results.count(results[0]) == 3:
            result = 1
            bal += (bet_amount * 8)
            print(f"{GREEN}You won!{RESET}")
        else:
            bal -= bet_amount
            print(f"{RED}You lost...{RESET}")
        
        if bal != 0:
            cont = input("Spin again? [Y, N]: ")

            while cont != "Y" and cont != "N":
                cont = input(f"{RED}Invalid Response.{RESET} Response must be either [Y, N]: ")
            
            if cont == "N":
                is_running = False
                print(f"Thank you for playing! Your final balance was {GREEN}${bal:.2f}{RESET}.")
            else:
                print(f"\nYour balance is now {GREEN}${bal:.2f}{RESET}.")
        
        else:
            is_running = False
            print(f"{RED}Womp womp... No more money for you :( {RESET})\n")

def print_intro():
    print(f"""\n{GREEN}
  /$$$$$$  /$$        /$$$$$$  /$$$$$$$$ /$$$$$$ 
 /$$__  $$| $$       /$$__  $$|__  $$__//$$__  $$
| $$  \__/| $$      | $$  \ $$   | $$  | $$  \__/
|  $$$$$$ | $$      | $$  | $$   | $$  |  $$$$$$ 
 \____  $$| $$      | $$  | $$   | $$   \____  $$
 /$$  \ $$| $$      | $$  | $$   | $$   /$$  \ $$
|  $$$$$$/| $$$$$$$$|  $$$$$$/   | $$  |  $$$$$$/
 \______/ |________/ \______/    |__/   \______/ 
            {RESET}\n""")
    
def init_slots():

    slots = ["🍑", "🍊", "🥝", "🍆"]

    return slots

if __name__ == "__main__":
    main()