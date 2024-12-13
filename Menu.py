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
    years = [year.strip() for year in years_input.split(',')]
    if all(year.isdigit() for year in years):
        return years
    return None

def get_value_by_row_year():
    row = input("\U0001F4C3 \033[1;36mEnter the row title: \033[0m").strip()
    year = input("\U0001F4C6 \033[1;36mEnter the year: \033[0m").strip()
    result = find_by_row_year(row, year, get_company())
    if result is not None:
        print(f"\U0001F4CA \033[1;32mResult for '{row}' in {year}: {result}\033[0m")
    else:
        print("\U0001F6AB \033[1;31mNo data found.\033[0m")

def get_values_by_row_years():
    row = input("\U0001F4C3 \033[1;36mEnter the row title: \033[0m").strip()
    years_input = input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m")
    years = sanitize_years_input(years_input)
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    result = find_by_row_years(row, years, get_company())
    print(f"\U0001F4CA \033[1;32mResults for '{row}' over years: {result}\033[0m")

def plot_values_by_row_years():
    row = input("\U0001F4C3 \033[1;36mEnter the row title: \033[0m").strip()
    years_input = input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m")
    years = sanitize_years_input(years_input)
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    plot_row_years(row, years, get_company())

def pretty_print(data):
    for year, value in data.items():
        formatted_value = f"{value:.4f}"
        print(f"{year}: {formatted_value}")

def calculate_current_ratio_menu():
    years_input = input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m")
    years = sanitize_years_input(years_input)
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    result = calculate_current_ratio(years, get_company())
    pretty_print(result)

def calculate_quick_ratio_menu():
    years_input = input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m")
    years = sanitize_years_input(years_input)
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    pretty_print(calculate_quick_ratio(years, get_company()))

def calculate_cash_ratio_menu():
    years_input = input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m")
    years = sanitize_years_input(years_input)
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    pretty_print(calculate_cash_ratio(years, get_company()))

def calculate_total_debt_ratio_menu():
    years_input = input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m")
    years = sanitize_years_input(years_input)
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    pretty_print(calculate_total_debt_ratio(years, get_company()))

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
