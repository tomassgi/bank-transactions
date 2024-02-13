# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# 

transactions = []

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List last 10 transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # deposit, jāpievieno jaunu transakciju
        # https://www.w3schools.com/python/python_lists_add.asp
        pass
    elif choice == '2':
        # withdraw, jāpievieno jaunu transakciju ar mīnus zīmi
        # https://www.w3schools.com/python/python_lists_add.asp
        pass
    elif choice == '3':
        # pārbaudīt atlikumu
        # jasummē visus saraksta elementus kopā ar ciklu palidzību
        # https://www.w3schools.com/python/python_for_loops.asp
        pass
    elif choice == '4':
        # rāda 10 pēdējas transakcijas
        # https://www.w3schools.com/python/python_lists_access.asp (Range of Negative Indexes)
        pass
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
