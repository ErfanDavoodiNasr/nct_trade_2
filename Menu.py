from Calculator import *


def display_menu():
    print("\n\U0001F4C8 Welcome to the Financial Analysis Tool! \U0001F4C8")
    print("====================================================")
    print("\U0001F4D1 Choose an option:")
    print("1️⃣  Find a specific value by row and year")
    print("2️⃣  Find values by row and multiple years")
    print("3️⃣  Plot values for a row over multiple years")
    print("4️⃣  Calculate Current Ratio")
    print("5️⃣  Calculate Quick Ratio")
    print("6️⃣  Calculate Cash Ratio")
    print("7️⃣  Calculate Total Debt Ratio")
    print("0️⃣  Exit")
    print("====================================================")


def main():
    while True:
        display_menu()
        try:
            choice = int(input("\U0001F4DD Enter your choice (0-7): "))

            if choice == 0:
                print("\U0001F44B Goodbye! Thank you for using the tool.")
                break

            elif choice == 1:
                row = input("\U0001F4C3 Enter the row title: ")
                year = input("\U0001F4C6 Enter the year: ")
                result = findByRowYear(row, year)
                if result is not None:
                    print(f"\U0001F4CA Result for '{row}' in {year}: {result}")
                else:
                    print("\U0001F6AB No data found.")

            elif choice == 2:
                row = input("\U0001F4C3 Enter the row title: ")
                years = input("\U0001F4C6 Enter the years (comma-separated): ").split(',')
                years = [year.strip() for year in years]
                result = findByRowYears(row, years)
                print(f"\U0001F4CA Results for '{row}' over years: {result}")

            elif choice == 3:
                row = input("\U0001F4C3 Enter the row title: ")
                years = input("\U0001F4C6 Enter the years (comma-separated): ").split(',')
                years = [year.strip() for year in years]
                plotRowYears(row, years)

            elif choice == 4:
                years = input("\U0001F4C6 Enter the years (comma-separated): ").split(',')
                years = [year.strip() for year in years]
                calculateCurrentRatio(years)

            elif choice == 5:
                years = input("\U0001F4C6 Enter the years (comma-separated): ").split(',')
                years = [year.strip() for year in years]
                calculateQuickRatio(years)

            elif choice == 6:
                years = input("\U0001F4C6 Enter the years (comma-separated): ").split(',')
                years = [year.strip() for year in years]
                calculateCashRatio(years)

            elif choice == 7:
                years = input("\U0001F4C6 Enter the years (comma-separated): ").split(',')
                years = [year.strip() for year in years]
                calculateTotalDebtRatio(years)

            else:
                print("\U0001F6AB Invalid choice. Please select a number between 0 and 7.")

        except ValueError:
            print("\U0001F6AB Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
