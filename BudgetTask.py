print("\n\n***Welcome to MyBudgetApp***\n")


class Budget:
    def __init__(self, categories = ["food", "clothing", "entertainment"], categories_balance = [1000,1000,1000]):
        self.categories = categories
        self.categories_balance = categories_balance

    # Begining of user experience with app: operations:deposit, withdraw, check balance and transfer
    def init_action(self):
        print("These are the operations available on this app\n  1. Deposit to a category\n  2. Withdraw from a category\n  3. Check category Balance\n  4. Transfer between categories")
        while True:
            action = int(input("What operation would you like to perform? Enter 1---4 respectively\nor enter 0 to exit the app: "))
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
        print("\nThese are the available categories: ")
        #prints all available categories with its index plus 1 as s/n
        for category in self.categories:
            print(self.categories.index(category) + 1, category)

        select_category = (int(input("Select category to deposit to: ")))
        selected_index = select_category - 1 #subtracts 1 from selected category s/n to get the actual index
        
        selected_category = self.categories[selected_index]
        print(f"You have chosen to deposit to the {selected_category} category")
        deposit_amount = int(input(f"How much will you like to deposit into the {selected_category} category? "))

        self.categories_balance[selected_index] += deposit_amount #deposit added to category balance as new balance
        print(f"You have successfully deposited N{deposit_amount} into the {selected_category} category")
        self.try_again()
        

    def withdraw(self):
        print("\nThese are the available categories: ")
        for category in self.categories:
            print(self.categories.index(category)+1, category)

        select_category = (int(input("Select category to withdraw from, enter 1--4 respectively for each category: ")))
        selected_index = select_category - 1
        selected_category = self.categories[selected_index]
        print(f"you have chosen to withdraw from the {selected_category} category")
        withdrawalAmount = int(input(f"how much will you like to withdraw from the {selected_category} category? "))
        #comparing withdrawal amount with available balance
        if withdrawalAmount >= self.categories_balance[selected_index]:
            print("You have insufficient balance!!!")
            self.try_again()
        else:
            self.categories_balance[selected_index] -= withdrawalAmount
            print(f"You have withdrawn {withdrawalAmount} successfully!")
            self.try_again()


    def get_balance(self):
        for category in self.categories:
            print(self.categories.index(category)+1, category)   
        select_category = (int(input("Select category to check balance of, enter 1--4 respectively for each category: ")))
        selected_index = select_category - 1
        selected_category = self.categories[selected_index]
        for category in self.categories_balance:
            balance = self.categories_balance[selected_index]
        print(f"{selected_category} balance: N{balance}")
        self.try_again()


    def transfer(self):
        print("\nThese are the available categories: ")
        for category in self.categories:
            print(self.categories.index(category)+1, category)

        transfer_from = int(input("\nWhat category would you like to transfer from: "))
        transfer_to = int(input("What category would you like to transfer to: "))

        if transfer_from == transfer_to:
            print("Destination category cannot be same as sender category, please try again!!!")
            self.transfer()

        transfer_from -=1
        transfer_to -=1
        selected_category_from = self.categories[transfer_from]
        selected_category_to = self.categories[transfer_to]
        transfer_amount = int(input("How much would you like to transfer: "))

        if transfer_amount >= self.categories_balance[transfer_from]:
            print("you have insufficient balance!!!")
            self.try_again()
        else:
            self.categories_balance[transfer_from] -= transfer_amount 
            self.categories_balance[transfer_to] += transfer_amount
            print(f"You have tranferred N{transfer_amount} from {selected_category_from} category to {selected_category_to} category")
            self.try_again()
    
    def try_again(self):
        #method to inquire if user wants to carry out another transaction, checks any invalid input and makes user try again if error is found.
        try:
            try_again = int(input("\nDo you want to carry out another transaction? Input 1 for (yes) or 2 for (no)? "))
        except:
            print("Invalid selection, try again!")
            self.try_again()
        if try_again == 1:
            self.init_action()
        elif try_again == 2:
            print("Thank you and have a nice day!!!")
            exit()
        

Budget().init_action()
