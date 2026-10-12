def main():
    blnce = 0.0  # Initializing the account balance to zero
    run = True

    print("--- Welcome to the Simple Python Bank ---")

    while run:
        print("\n1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\nYour current balance is: $", round(blnce, 2))
            
        elif choice == '2':
            amt = float(input("\nEnter amount to deposit: $"))
            if amt > 0:
                blnce += amt
                print("$", round(amt, 2), "deposited successfully!")
            else:
                print("Invalid amount. Please enter a value greater than 0.")
                
        elif choice == '3':
            amt = float(input("\nEnter amount to withdraw: $"))
            if amt > blnce:
                print("Insufficient funds! Transaction cancelled.")
            elif amt <= 0:
                print("Invalid amount. Please enter a value greater than 0.")
            else:
                blnce -= amt
                print("$", round(amt, 2), "withdrawn successfully!")
                
        elif choice == '4':
            print("\nThank you for using Python Bank. Goodbye!")
            run = False
            
        else:
            print("Invalid choice. Please pick an option between 1 and 4.")

if __name__ == "__main__":
    main()
