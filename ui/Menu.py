from ui.CalculatorMenu import *
from ui.DataMenu import *


def display_menu():
    print("\n\U0001F680 \033[1;32m*** Welcome to the Financial Analysis Tool! ***\033[0m \U0001F680")
    print("\033[1;34m========================================================\033[0m")
    print("\U0001F4D1 \033[1;36mChoose an option:\033[0m")
    print(" 1️⃣  \033[1;33mFind a specific value by row and year\033[0m \U0001F4C6")
    print(" 2️⃣  \033[1;33mFind values by row and multiple years\033[0m \U0001F4C5")
    print(" 3️⃣  \033[1;33mPlot values for a row over multiple years\033[0m \U0001F4CA")
    print(" 4️⃣  \033[1;33mCalculate Current Ratio\033[0m \U0001F4B0")
    print(" 5️⃣  \033[1;33mCalculate Quick Ratio\033[0m \U0001F4C8")
    print(" 6️⃣  \033[1;33mCalculate Cash Ratio\033[0m \U0001F4B5")
    print(" 7️⃣  \033[1;33mCalculate Total Debt Ratio\033[0m \U0001F9FE")
    print(" 0️⃣  \033[1;31mExit\033[0m \U0001F44B")
    print("\033[1;34m========================================================\033[0m")


def main():
    while True:
        display_menu()
        try:
            choice = int(input("\U0001F4DD \033[1;35mEnter your choice (0-7): \033[0m"))

            match choice:
                case 0:
                    print("\U0001F44B \033[1;32mGoodbye! Thank you for using the tool.\033[0m")
                    break
                case 1:
                    get_value_by_row_year()
                case 2:
                    get_values_by_row_years()
                case 3:
                    plot_values_by_row_years()
                case 4:
                    calculate_current_ratio_menu()
                case 5:
                    calculate_quick_ratio_menu()
                case 6:
                    calculate_cash_ratio_menu()
                case 7:
                    calculate_total_debt_ratio_menu()
                case _:
                    print("\U0001F6AB \033[1;31mInvalid choice. Please select a number between 0 and 7.\033[0m")
        except ValueError:
            print("\U0001F6AB \033[1;31mInvalid input. Please enter a valid number.\033[0m")


if __name__ == "__main__":
    main()
