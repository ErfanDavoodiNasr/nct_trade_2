import pandas as pd
import matplotlib.pyplot as plt


def findByRowYear(row,year):
    df = pd.read_csv('data/fajr.csv', encoding='utf-8')
    financial_facilities_row = df[df['عنوان'].str.contains(row, na=False)]
    if financial_facilities_row.empty:
        return None
    else:
        return financial_facilities_row[year].values[0]


def findByRowYears(row, years):
    df = pd.read_csv('data/fajr.csv', encoding='utf-8')
    financial_facilities_row = df[df['عنوان'].str.contains(row, na=False)]
    if financial_facilities_row.empty:
        return None
    result = {}
    for year in years:
        if year in df.columns:
            value = financial_facilities_row[year].values[0]
            result[year] = value if pd.notna(value) else None
        else:
            result[year] = None
    return result



def plotRowYears(row, years):
    data = findByRowYears(row, years)

    if not data or (hasattr(data, 'any') and not data.any()) or len(data) == 0:
        print("Error: No data found for the given row.")
        return

    filtered_data = {year: value for year, value in data.items() if value is not None}

    if not filtered_data:
        print("Error: No valid data found for the given row and years.")
        return

    x = list(filtered_data.keys())
    y = list(filtered_data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label=row)
    plt.xlabel('Years')
    plt.ylabel('Values')
    plt.title(f'Data Plot for "{row}"')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()



def calculateCurrentRatio(years):
    # دریافت دارایی‌های جاری
    assets = findByRowYears("جمع دارايی های جاری", years)
    if not assets:
        print("Error: Could not find asset data.")
        return None

    # دریافت بدهی‌های جاری
    liabilities = findByRowYears("جمع بدهی های جاری", years)
    if not liabilities:
        print("Error: Could not find liability data.")
        return None

    # محاسبه نسبت جاری
    current_ratios = {}
    for year in years:
        asset_value = assets.get(year)
        liability_value = liabilities.get(year)

        if asset_value is None or liability_value is None or liability_value == 0:
            current_ratios[year] = None
        else:
            current_ratios[year] = asset_value / liability_value

    # فیلتر کردن داده های خالی
    filtered_years = [year for year in years if current_ratios.get(year) is not None]
    filtered_ratios = [current_ratios[year] for year in filtered_years]

    # بررسی داده‌های کافی برای رسم نمودار
    if not filtered_ratios:
        print("Error: No valid data available to plot.")
        return

    # رسم نمودار و تنظیمات
    plt.figure(figsize=(5, 5))
    plt.plot(filtered_years, filtered_ratios, marker='o', linestyle='-', color='b', label="Current Ratio")
    plt.xlabel('Years')
    plt.ylabel('Current Ratio')
    plt.title('Current Ratio Over Years')
    plt.grid(True, linestyle='--', alpha=0)
    plt.legend()
    plt.show()

    return current_ratios



def calculateQuickRatio(years):
    # دریافت دارایی‌های جاری
    assets = findByRowYears("جمع دارايی های جاری", years)
    if not assets:
        print("Error: Could not find asset data.")
        return None

    # دریافت موجودی کالا
    inventory = findByRowYears("موجودی مواد و کالا", years)
    if not inventory:
        print("Error: Could not find inventory data.")
        return None

    # دریافت بدهی‌های جاری
    liabilities = findByRowYears("جمع بدهی های جاری", years)
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
            quick_ratios[year] = None
        else:
            quick_ratios[year] = (asset_value - inventory_value) / liability_value

    # فیلتر کردن داده های خالی
    filtered_years = [year for year in years if quick_ratios.get(year) is not None]
    filtered_ratios = [quick_ratios[year] for year in filtered_years]

    # بررسی داده‌های کافی برای رسم نمودار
    if not filtered_ratios:
        print("Error: No valid data available to plot.")
        return

    # رسم نمودار و تنظیمات
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_years, filtered_ratios, marker='o', linestyle='-', color='b', label="Quick Ratio")
    plt.xlabel('Years')
    plt.ylabel('Quick Ratio')
    plt.title('Quick Ratio Over Years')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

    return quick_ratios




def calculateCashRatio(years):
    # دریافت وجه نقد
    cash = findByRowYears("موجودی نقد", years)
    if not cash:
        print("Error: Could not find cash data.")
        return None

    # دریافت بدهی‌های جاری
    liabilities = findByRowYears("جمع بدهی های جاری", years)
    if not liabilities:
        print("Error: Could not find liability data.")
        return None

    # محاسبه نسبت وجه نقد
    cash_ratios = {}
    for year in years:
        cash_value = cash.get(year)
        liability_value = liabilities.get(year)

        if cash_value is None or liability_value is None or liability_value == 0:
            cash_ratios[year] = None
        else:
            cash_ratios[year] = cash_value / liability_value

    # حذف سال‌هایی که داده ندارند
    filtered_years = [year for year in years if cash_ratios.get(year) is not None]
    filtered_ratios = [cash_ratios[year] for year in filtered_years]

    # بررسی داده‌های کافی برای رسم نمودار
    if not filtered_ratios:
        print("Error: No valid data available to plot.")
        return

    # رسم نمودار و تنظیمات
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_years, filtered_ratios, marker='o', linestyle='-', color='b', label="Cash Ratio")
    plt.xlabel('Years')
    plt.ylabel('Cash Ratio')
    plt.title('Cash Ratio Over Years')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

    return cash_ratios



def calculateTotalDebtRatio(years):
    # دریافت بدهی‌های جاری
    current_liabilities = findByRowYears("جمع بدهی های جاری", years)
    if not current_liabilities:
        print("Error: Could not find current liabilities data.")
        return None

    # دریافت بدهی‌های بلندمدت
    long_term_liabilities = findByRowYears("جمع بدهی های بلندمدت", years)
    if not long_term_liabilities:
        print("Error: Could not find long-term liabilities data.")
        return None

    # دریافت مجموع دارایی‌ها
    total_assets = findByRowYears("جمع دارایی ها", years)
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
            debt_ratios[year] = None
        else:
            debt_ratios[year] = (current_liab + long_term_liab) / total_asset

    # حذف سال‌هایی که داده ندارند
    filtered_years = [year for year in years if debt_ratios.get(year) is not None]
    filtered_ratios = [debt_ratios[year] for year in filtered_years]

    # بررسی داده‌های کافی برای رسم نمودار
    if not filtered_ratios:
        print("Error: No valid data available to plot.")
        return

    # رسم نمودار
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_years, filtered_ratios, marker='o', linestyle='-', color='b', label="Total Debt Ratio")
    plt.xlabel('Years')
    plt.ylabel('Total Debt Ratio')
    plt.title('Total Debt Ratio Over Years')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

    return debt_ratios



