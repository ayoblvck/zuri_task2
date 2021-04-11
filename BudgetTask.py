print("\n\n***Welcome to MyBudgetApp***\n")


class Budget:
    def __init__(self, categories = ["food", "clothing", "entertainment"], categories_balance = [1000,1000,1000]):
        self.categories = categories
        self.categories_balance = categories_balance


    def init_action(self):
        print("These are the operations available on this app\n  1. Deposit to a category\n  2. Withdraw from a category\n  3. Check category Balance\n  4. Transfer between categories")
        while True:
            action = int(input("what operation would you like to perform? Enter 1---4 respectively\nor enter 0 to exit the app: "))
            if action ==1:
                self.deposit()
                False
            elif action == 2:
                self.withdraw()
                False
            elif action == 3:
                self.get_balance()
                False
            elif action == 4: 
                self.transfer()
                False
            elif action ==0:
                exit()
            else:
                print("invalid input, try again")

   
    def deposit(self):
        print("These are the available categories: ")
        for category in self.categories:
            print(self.categories.index(category) + 1, category)
        select_category = (int(input("Select category to deposit to: ")))
        selected_index = select_category - 1
        selected_category = self.categories[selected_index]
        print(f"You have chosen to deposit to the {selected_category} category")
        deposit_amount = int(input(f"How much will you like to deposit into the {selected_category} category? "))
        self.categories_balance[selected_index] += deposit_amount
        print(f"You have successfully deposited N{deposit_amount} into the {selected_category} category")
        Budget().try_again()
        

    def withdraw(self):
        print("These are the available categories: ")
        for category in self.categories:
            print(self.categories.index(category)+1, category)
        select_category = (int(input("select category to withdraw from: ")))
        selected_index = select_category - 1
        selected_category = self.categories[selected_index]
        print(f"you have chosen to withdraw from the {selected_category} category")
        withdrawalAmount = int(input(f"how much will you like to withdraw from the {selected_category} category? "))
        if withdrawalAmount >= self.categories_balance[selected_index]:
            print("You have insufficient balance!!!")
            Budget().try_again()
        else:
            self.categories_balance[selected_index] -= withdrawalAmount
            print(f"you have withdrawn {withdrawalAmount} successfully!")
            Budget().try_again()


    def get_balance(self):
        for category in self.categories:
            print(self.categories.index(category)+1, category)   
        select_category = (int(input("select category to check balance of: ")))
        selected_index = select_category - 1
        selected_category = self.categories[selected_index]
        for category in self.categories_balance:
            balance = self.categories_balance[selected_index]
        print(f"{selected_category} balance: N{balance}")
        Budget().try_again()


    def transfer(self):
        print("These are the available categories: ")
        for category in self.categories:
            print(self.categories.index(category)+1, category)
        transfer_from = int(input("what category would you like to transfer from: "))
        transfer_to = int(input("what category would you like to transfer to: "))
        if transfer_from == transfer_to:
            print("destination category cannot be same as sender category, please try again!!!")
            Budget().transfer()
        transfer_from -=1
        transfer_to -=1
        selected_category_from = self.categories[transfer_from]
        selected_category_to = self.categories[transfer_to]
        transfer_amount = int(input("How much would you like to transfer: "))
        if transfer_amount >= self.categories_balance[transfer_from]:
            print("you have insufficient balance!!!")
            Budget().try_again()
        else:
            self.categories_balance[transfer_from] -= transfer_amount 
            self.categories_balance[transfer_to] += transfer_amount
            print(f"you have tranferred N{transfer_amount} from {selected_category_from} category to {selected_category_to} category")
            Budget().try_again()
    
    def try_again(self):
        try:
            try_again = int(input("Do you want to carry out another transaction? Input 1 for (yes) or 2 for (no)? "))
        except:
            print("invalid selection, try again!")
            Budget().try_again()
        if try_again == 1:
            Budget().init_action()
        elif try_again == 2:
            print("Thank you and have a nice day!!!")
            exit()
        

Budget().init_action()
