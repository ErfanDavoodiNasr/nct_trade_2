from Calculator import *

def display_menu():
    print("\n\U0001F680 \033[1;32mWelcome to the Financial Analysis Tool!\033[0m \U0001F680")
    print("\033[1;34m====================================================\033[0m")
    print("\U0001F4D1 \033[1;36mChoose an option:\033[0m")
    print("1️⃣  \033[1;33mFind a specific value by row and year\033[0m")
    print("2️⃣  \033[1;33mFind values by row and multiple years\033[0m")
    print("3️⃣  \033[1;33mPlot values for a row over multiple years\033[0m")
    print("4️⃣  \033[1;33mCalculate Current Ratio\033[0m")
    print("5️⃣  \033[1;33mCalculate Quick Ratio\033[0m")
    print("6️⃣  \033[1;33mCalculate Cash Ratio\033[0m")
    print("7️⃣  \033[1;33mCalculate Total Debt Ratio\033[0m")
    print("0️⃣  \033[1;31mExit\033[0m")
    print("\033[1;34m====================================================\033[0m")

def sanitize_years_input(years_input):
    return [year.strip() for year in years_input.split(',') if year.strip().isdigit()]

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\U0001F4DD \033[1;35mEnter your choice (0-7): \033[0m"))

            if choice == 0:
                print("\U0001F44B \033[1;32mGoodbye! Thank you for using the tool.\033[0m")
                break

            elif choice == 1:
                row = input("\U0001F4C3 \033[1;36mEnter the row title: \033[0m").strip()
                year = input("\U0001F4C6 \033[1;36mEnter the year: \033[0m").strip()
                result = findByRowYear(row, year)
                if result is not None:
                    print(f"\U0001F4CA \033[1;32mResult for '{row}' in {year}: {result}\033[0m")
                else:
                    print("\U0001F6AB \033[1;31mNo data found.\033[0m")

            elif choice == 2:
                row = input("\U0001F4C3 \033[1;36mEnter the row title: \033[0m").strip()
                years = sanitize_years_input(input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m"))
                if not years:
                    print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
                    continue
                result = findByRowYears(row, years)
                print(f"\U0001F4CA \033[1;32mResults for '{row}' over years: {result}\033[0m")

            elif choice == 3:
                row = input("\U0001F4C3 \033[1;36mEnter the row title: \033[0m").strip()
                years = sanitize_years_input(input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m"))
                if not years:
                    print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
                    continue
                plotRowYears(row, years)

            elif choice == 4:
                years = sanitize_years_input(input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m"))
                if not years:
                    print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
                    continue
                calculateCurrentRatio(years)

            elif choice == 5:
                years = sanitize_years_input(input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m"))
                if not years:
                    print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
                    continue
                calculateQuickRatio(years)

            elif choice == 6:
                years = sanitize_years_input(input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m"))
                if not years:
                    print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
                    continue
                calculateCashRatio(years)

            elif choice == 7:
                years = sanitize_years_input(input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m"))
                if not years:
                    print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
                    continue
                calculateTotalDebtRatio(years)

            else:
                print("\U0001F6AB \033[1;31mInvalid choice. Please select a number between 0 and 7.\033[0m")

        except ValueError:
            print("\U0001F6AB \033[1;31mInvalid input. Please enter a valid number.\033[0m")

if __name__ == "__main__":
    main()
