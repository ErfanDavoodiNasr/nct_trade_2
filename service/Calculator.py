from service.Data import *


def calculate_current_ratio(years, company):
    # دریافت دارایی‌های جاری
    assets = find_by_row_years("جمع دارايی های جاری", years, company)
    if not assets:
        print("Error: Could not find asset data.")
        return None

    # دریافت بدهی‌های جاری
    liabilities = find_by_row_years("جمع بدهی های جاری", years, company)
    if not liabilities:
        print("Error: Could not find liability data.")
        return None

    # محاسبه نسبت جاری
    current_ratios = {}
    for year in years:
        asset_value = assets.get(year)
        liability_value = liabilities.get(year)

        if asset_value is None or liability_value is None or liability_value == 0:
            pass
        else:
            current_ratios[year] = asset_value / liability_value

    return current_ratios


def calculate_quick_ratio(years, company):
    # دریافت دارایی‌های جاری
    assets = find_by_row_years("جمع دارايی های جاری", years, company)
    if not assets:
        print("Error: Could not find asset data.")
        return None

    # دریافت موجودی کالا
    inventory = find_by_row_years("موجودی مواد و کالا", years, company)
    if not inventory:
        print("Error: Could not find inventory data.")
        return None

    # دریافت بدهی‌های جاری
    liabilities = find_by_row_years("جمع بدهی های جاری", years, company)
    if not liabilities:
        print("Error: Could not find liability data.")
        return None

    # محاسبه نسبت آنی
    quick_ratios = {}
    for year in years:
        asset_value = assets.get(year)
        inventory_value = inventory.get(year)
        liability_value = liabilities.get(year)

        if (
                asset_value is None
                or inventory_value is None
                or liability_value is None
                or liability_value == 0
        ):
            pass
        else:
            quick_ratios[year] = (asset_value - inventory_value) / liability_value

    return quick_ratios


def calculate_cash_ratio(years, company):
    # دریافت وجه نقد
    cash = find_by_row_years("موجودی نقد", years, company)
    if not cash:
        print("Error: Could not find cash data.")
        return None

    # دریافت بدهی‌های جاری
    liabilities = find_by_row_years("جمع بدهی های جاری", years, company)
    if not liabilities:
        print("Error: Could not find liability data.")
        return None

    # محاسبه نسبت وجه نقد
    cash_ratios = {}
    for year in years:
        cash_value = cash.get(year)
        liability_value = liabilities.get(year)

        if cash_value is None or liability_value is None or liability_value == 0:
            pass
        else:
            cash_ratios[year] = cash_value / liability_value

    return cash_ratios


def calculate_total_debt_ratio(years, company):
    # دریافت بدهی‌های جاری
    current_liabilities = find_by_row_years("جمع بدهی های جاری", years, company)
    if not current_liabilities:
        print("Error: Could not find current liabilities data.")
        return None

    # دریافت بدهی‌های بلندمدت
    long_term_liabilities = find_by_row_years("جمع بدهی های بلندمدت", years, company)
    if not long_term_liabilities:
        print("Error: Could not find long-term liabilities data.")
        return None

    # دریافت مجموع دارایی‌ها
    total_assets = find_by_row_years("جمع دارایی ها", years, company)
    if not total_assets:
        print("Error: Could not find total assets data.")
        return None

    # محاسبه نسبت بدهی
    debt_ratios = {}
    for year in years:
        current_liab = current_liabilities.get(year)
        long_term_liab = long_term_liabilities.get(year)
        total_asset = total_assets.get(year)

        if (
                current_liab is None
                or long_term_liab is None
                or total_asset is None
                or total_asset == 0
        ):
            pass
        else:
            debt_ratios[year] = (current_liab + long_term_liab) / total_asset

    return debt_ratios
