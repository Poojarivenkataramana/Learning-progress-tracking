# Project 2 : Daily Expense Tracker:-
import matplotlib.pyplot as plt

days = list(map(int,input("Enter Days (1 - 7): ").split()))
Expenses = list(map(int,input("Enter expenses for each day:: ").split()))

if len(days) != len(Expenses):
    print("Error: Days and Expenses count must match!")
else:

    # Tracking Highest Expense Day

    Highest_Expense = max(Expenses)
    Highest_Expense_index = Expenses.index(Highest_Expense)
    Highest_Expense_position = days[Highest_Expense_index]

    # Tracking Lowest Expense Day
    Lowest_Expense = min(Expenses)
    Lowest_Expense_index = Expenses.index(Lowest_Expense)
    Lowest_Expense_position = days[Lowest_Expense_index]

    # Adding Title To The Graph:-

    plt.title("My Daily Expense Tracker")
    plt.xlabel("Days")
    plt.ylabel("Expenses of Each Day")

    plt.plot(days,Expenses,color = "blue",linestyle = "--",linewidth = 3,marker = 's',label = "Daily Expenses")
    plt.plot(Highest_Expense_position, Highest_Expense, color="red", marker='s', markersize=10, label="Highest Expense Day")
    plt.plot(Lowest_Expense_position, Lowest_Expense, color='black', marker='s', markersize=10, label="Lowest Expense Day")
    plt.text(Highest_Expense_position, Highest_Expense + 2, "Highest", color='red')
    plt.text(Lowest_Expense_position, Lowest_Expense - 2, "Lowest", color='black')

    print(f"Highest Expense  Day is : {Highest_Expense_position}")
    print(f"Highest Expense is: {Highest_Expense}")

    print(f"Lowest Expense Day is: {Lowest_Expense_position}")
    print(f"Lowest Expense is: {Lowest_Expense}")


    plt.legend()
    plt.grid()
    plt.show()
