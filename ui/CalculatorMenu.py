from service.Calculator import *
from util.Help import *


def calculate_current_ratio_menu():
    years = get_valid_years()
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    result = calculate_current_ratio(years, get_company())
    display_result("Current Ratio", result)


def calculate_quick_ratio_menu():
    years = get_valid_years()
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    result = calculate_quick_ratio(years, get_company())
    display_result("Quick Ratio", result)


def calculate_cash_ratio_menu():
    years = get_valid_years()
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    result = calculate_cash_ratio(years, get_company())
    display_result("Cash Ratio", result)


def calculate_total_debt_ratio_menu():
    years = get_valid_years()
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    result = calculate_total_debt_ratio(years, get_company())
    display_result("Total Debt Ratio", result)