def get_valid_years():
    valid_years = {"1397", "1398", "1399", "1400", "1401", "1402"}

    while True:
        years_input = input("\U0001F4C6 \033[1;36mEnter the years (comma-separated): \033[0m")
        years = sanitize_years_input(years_input)

        if years and all(year in valid_years for year in years):
            return years

        print("\033[1;31mInvalid input. Please enter valid years.\033[0m")


def sanitize_years_input(years_input):
    years = [year.strip() for year in years_input.split(',')]
    if all(year.isdigit() for year in years):
        return years
    return None


# display for print funcs result
def display_result(title, data):
    print(f"\n\U0001F4C3 \033[1;36m{title}:\033[0m")
    print("\033[1;34m--------------------------------------------------------\033[0m")

    if data is None:
        print("\U0001F6AB \033[1;31mNo data available\033[0m")
    else:
        for key, value in data.items():
            if value is None:
                print(f"\U0001F4C6 {key}: \033[1;31mValue is NaN\033[0m")
            else:
                print(f"\U0001F4C6 {key}: \033[1;32m{value:.4f}\033[0m")

    print("\033[1;34m--------------------------------------------------------\033[0m")


def get_company():
    print_companies()

    while True:
        company = input("\U0001F4C3 \033[1;36mChoose an option: \033[0m").strip()
        if company == "1":
            return '../data/ذوب.csv'
        if company == "2":
            return "../data/شبندر.csv"
        if company == "3":
            return "../data/فولاد.csv"
        else:
            print("\033[1;31mInvalid input. Please enter valid company name.\033[0m")
            continue


def print_companies():
    companies = ["ذوب", "شبندر", "فولاد"]
    max_width = max(len(company) for company in companies) + 10
    border = f"\u250c{''.ljust(max_width, '\u2500')}\u2510"
    separator = f"\u251c{''.ljust(max_width, '\u2500')}\u2524"
    footer = f"\u2514{''.ljust(max_width, '\u2500')}\u2518"
    print(border)
    print(
        f"| {f'\033[1;34m\u0644\u06cc\u0633\u062a \u0634\u0631\u06a9\u062a\u200c\u0647\u0627\033[0m'.center(max_width)} |")
    print(separator)
    for i, company in enumerate(companies, 1):
        index = f"\033[1;33m{i:2d}.\033[0m"
        print(f"| {index} {company.ljust(max_width - len(index) - 2)} |")
    print(footer)
