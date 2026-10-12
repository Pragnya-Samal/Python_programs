def main():
    bread_p = 25.00
    pastry_p = 40.00
    cake_p = 250.00
    biscuit_p = 60.00
    cookies_p = 80.00

    bread_c = 0
    pastry_c = 0
    cake_c = 0
    biscuit_c = 0
    cookies_c = 0

    is_running = True

    print("--- Welcome to the Custom Python Bakery ---")

    while is_running:
        print("\n==============================")
        print("To buy Bread click 1 (Rs.", bread_p, ")")
        print("To buy Pastry click 2 (Rs.", pastry_p, ")")
        print("To buy Cake click 3 (Rs.", cake_p, ")")
        print("To buy Biscuit click 4 (Rs.", biscuit_p, ")")
        print("To buy Cookies click 5 (Rs.", cookies_p, ")")
        print("6. View Cart & Total")
        print("7. Checkout & Exit")
        print("==============================")

        choice = input("Select an option (1-7): ")

        if choice == '1':
            quant = int(input("\nHow many packets of bread? "))
            if quant > 0:
                bread_c += quant
                print("Added", quant, "Bread to your cart!")
            else:
                print("Please enter a number greater than 0.")

        elif choice == '2':
            quant = int(input("\nHow many pastries? "))
            if quant > 0:
                pastry_c += quant
                print("Added", quant, "Pastry to your cart!")
            else:
                print("Please enter a number greater than 0.")

        elif choice == '3':
            quant = int(input("\nHow many cakes? "))
            if quant > 0:
                cake_c += quant
                print("Added", quant, "Cake(s) to your cart!")
            else:
                print("Please enter a number greater than 0.")

        elif choice == '4':
            quant = int(input("\nHow many packets of biscuits? "))
            if quant > 0:
                biscuit_c += quant
                print("Added", quant, "Biscuit pack(s) to your cart!")
            else:
                print("Please enter a number greater than 0.")

        elif choice == '5':
            quant = int(input("\nHow many boxes of cookies? "))
            if quant > 0:
                cookies_c += quant
                print("Added", quant, "Cookies box(es) to your cart!")
            else:
                print("Please enter a number greater than 0.")

        elif choice == '6':
            bread_cost = bread_c * bread_p
            pastry_cost = pastry_c * pastry_p
            cake_cost = cake_c * cake_p
            biscuit_cost = biscuit_c * biscuit_p
            cookies_cost = cookies_c * cookies_p
            
            total = bread_cost + pastry_cost + cake_cost + biscuit_cost + cookies_cost
            
            print("\n--- Current Cart Status ---")
            print("Bread:", bread_c)
            print("Pastry:", pastry_c)
            print("Cake:", cake_c)
            print("Biscuit:", biscuit_c)
            print("Cookies:", cookies_c)
            print("Your Current Total: Rs.", total)

        elif choice == '7':
            bread_cost = bread_c * bread_p
            pastry_cost = pastry_c * pastry_p
            cake_cost = cake_c * cake_p
            biscuit_cost = biscuit_c * biscuit_p
            cookies_cost = cookies_c * cookies_p
            
            final_total = bread_cost + pastry_cost + cake_cost + biscuit_cost + cookies_cost
            
            print("\n--- Final Bill ---")
            if bread_c > 0:
                print("- Bread x", bread_c, ": Rs.", bread_cost)
            if pastry_c > 0:
                print("- Pastry x", pastry_c, ": Rs.", pastry_cost)
            if cake_c > 0:
                print("- Cake x", cake_c, ": Rs.", cake_cost)
            if biscuit_c > 0:
                print("- Biscuit x", biscuit_c, ": Rs.", biscuit_cost)
            if cookies_c > 0:
                print("- Cookies x", cookies_c, ": Rs.", cookies_cost)
            print("------------------------------")
            print("Total Amount Paid: Rs.", final_total)
            print("Thank you for visiting! Have a great day!")
            is_running = False

        else:
            print("Invalid choice. Please pick an option between 1 and 7.")

if __name__ == "__main__":
    main()
