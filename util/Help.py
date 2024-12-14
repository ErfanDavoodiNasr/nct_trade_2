def sanitize_years_input(years_input):
    years = [year.strip() for year in years_input.split(',')]
    if all(year.isdigit() for year in years):
        return years
    return None


def display_result(title, data):
    print(f"\n\U0001F4C3 \033[1;36m{title}:\033[0m")
    print("\033[1;34m--------------------------------------------------------\033[0m")
    for key, value in data.items():
        print(f"\U0001F4C6 {key}: \033[1;32m{value:.4f}\033[0m")
    print("\033[1;34m--------------------------------------------------------\033[0m")


def get_company():
    companies = {"ذوب", "شبندر", "فولاد"}
    print(" ".join(companies))

    company = input("\U0001F4C3 \033[1;36menter company name: \033[0m").strip()
    if company == "ذوب":
        return '../data/ذوب.csv'
    if company == "شبندر":
        return "../data/شبندر.csv"
    if company == "فولاد":
        return "../data/فولاد.csv"