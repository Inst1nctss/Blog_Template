bal = 100

BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

def main ():
    while True:
        print (f"{BLUE}1. Check Balance{ENDC}")
        print (f"{GREEN}2. Withdraw Money{ENDC}")
        print (f"{GREEN}3. Deposit Money{ENDC}")
        print (f"{RED}4. Exit Application{ENDC}")
        choice = input(f"{GREEN}What do you want to do? ENTER THE NUMBER {ENDC}")
   
        if choice == "1":
            CheckBal(bal)
        if choice == "2":
            Withdraw()
        if choice == "3":
            Deposit()
        if choice == "4":
            print(f"{RED}Thank you, Have a nice day{ENDC}")
            break
       
   
def CheckBal(bal):
    print(f"{BLUE}Your balance is {bal}{ENDC}")

def Withdraw():
    global bal
    amount = float (input(f"{GREEN}How much do you want to Withdraw?{ENDC}"))
    if amount > bal:
        print(f"{RED}Invalid amount. Please enter valid amount.{ENDC}")
    else:
        bal -= amount
        print (f"{RED}Money Withdrawn:  {amount}{ENDC}")
        print (f"{GREEN}Your new balance is: {bal}{ENDC}")
def Deposit():
    global bal
    amount = float (input(f"{GREEN}How much do you want to Deposit?{ENDC}"))
    if amount <= 0:
        print(f"{RED}Invalid amount. Please enter valid amount{ENDC}")
    else:
        bal += amount
        print (f"{RED}Money Deposited: {amount}{ENDC}")
        print (f"{GREEN}Your new balance is: {bal}{ENDC}")


main()