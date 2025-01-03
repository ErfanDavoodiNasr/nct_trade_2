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


def calculate_debt_to_equity_ratio(years, company):
    # دریافت مجموع بدهی‌ها
    total_liabilities = find_by_row_years("جمع بدهی ها", years, company)
    if not total_liabilities:
        print("Error: Could not find total liabilities data.")
        return None

    # دریافت مجموع حقوق صاحبان سهام
    total_equity = find_by_row_years("جمع حقوق صاحبان سهام", years, company)
    if not total_equity:
        print("Error: Could not find total equity data.")
        return None

    # محاسبه نسبت بدهی به حقوق صاحبان سهام
    debt_to_equity_ratios = {}
    for year in years:
        total_liab = total_liabilities.get(year)
        total_eq = total_equity.get(year)

        if (
                total_liab is None
                or total_eq is None
                or total_eq == 0
        ):
            pass
        else:
            debt_to_equity_ratios[year] = total_liab / total_eq

    return debt_to_equity_ratios


def calculate_equity_multiplier(years, company):
    # دریافت مجموع دارایی‌ها
    total_assets = find_by_row_years("جمع دارایی ها", years, company)
    if not total_assets:
        print("Error: Could not find total assets data.")
        return None

    # دریافت مجموع حقوق صاحبان سهام
    total_equity = find_by_row_years("جمع حقوق صاحبان سهام", years, company)
    if not total_equity:
        print("Error: Could not find total equity data.")
        return None

    # محاسبه ضریب مالکانه
    equity_multipliers = {}
    for year in years:
        total_asset = total_assets.get(year)
        total_eq = total_equity.get(year)

        if (
                total_asset is None
                or total_eq is None
                or total_eq == 0
        ):
            pass
        else:
            equity_multipliers[year] = total_asset / total_eq

    return equity_multipliers


def calculate_long_term_debt_ratio(years, company):
    # دریافت بدهی‌های بلندمدت
    long_term_liabilities = find_by_row_years("جمع بدهی های بلندمدت", years, company)
    if not long_term_liabilities:
        print("Error: Could not find long-term liabilities data.")
        return None

    # دریافت مجموع حقوق صاحبان سهام
    total_equity = find_by_row_years("جمع حقوق صاحبان سهام", years, company)
    if not total_equity:
        print("Error: Could not find total equity data.")
        return None

    # محاسبه نسبت بدهی بلندمدت
    long_term_debt_ratios = {}
    for year in years:
        long_term_liab = long_term_liabilities.get(year)
        total_eq = total_equity.get(year)

        if (
                long_term_liab is None
                or total_eq is None
                or (long_term_liab + total_eq) == 0
        ):
            pass
        else:
            long_term_debt_ratios[year] = long_term_liab / (long_term_liab + total_eq)

    return long_term_debt_ratios


def calculate_earned_interest_time_ratio(years, company):
    # دریافت سود قبل از بهره و مالیات
    earnings_before_interest_and_tax = find_by_row_years("سود قبل از بهره و مالیات", years, company)
    if not earnings_before_interest_and_tax:
        print("Error: Could not find earnings before interest and tax data.")
        return None

    # دریافت هزینه بهره
    interest_expense = find_by_row_years("هزینه بهره", years, company)
    if not interest_expense:
        print("Error: Could not find interest expense data.")
        return None

    # محاسبه نسبت دفعات پوشش هزینه بهره
    earned_interest_time_ratios = {}
    for year in years:
        ebit = earnings_before_interest_and_tax.get(year)
        interest = interest_expense.get(year)

        if (
                ebit is None
                or interest is None
                or interest == 0
        ):
            pass
        else:
            earned_interest_time_ratios[year] = ebit / interest

    return earned_interest_time_ratios


def calculate_cash_coverage_ratio(years, company):
    # دریافت استهلاک
    depreciation = find_by_row_years("استهلاک", years, company)
    if not depreciation:
        print("Error: Could not find depreciation data.")
        return None

    # دریافت سود قبل از بهره و مالیات
    earnings_before_interest_and_tax = find_by_row_years("سود قبل از بهره و مالیات", years, company)
    if not earnings_before_interest_and_tax:
        print("Error: Could not find earnings before interest and tax data.")
        return None

    # دریافت هزینه بهره
    interest_expense = find_by_row_years("هزینه بهره", years, company)
    if not interest_expense:
        print("Error: Could not find interest expense data.")
        return None

    # محاسبه نسبت پوشش نقدی بهره
    cash_coverage_ratios = {}
    for year in years:
        dep = depreciation.get(year)
        ebit = earnings_before_interest_and_tax.get(year)
        interest = interest_expense.get(year)

        if (
                dep is None
                or ebit is None
                or interest is None
                or interest == 0
        ):
            pass
        else:
            cash_coverage_ratios[year] = (dep + ebit) / interest

    return cash_coverage_ratios


def calculate_inventory_turnover_ratio(years, company):
    # دریافت بهای تمام شده کالای فروش رفته
    cost_of_goods_sold = find_by_row_years("بهای تمام شده کالای فروش رفته", years, company)
    if not cost_of_goods_sold:
        print("Error: Could not find cost of goods sold data.")
        return None

    # دریافت موجودی پایان دوره
    ending_inventory = find_by_row_years("موجودی پایان دوره", years, company)
    if not ending_inventory:
        print("Error: Could not find ending inventory data.")
        return None

    # محاسبه نسبت گردش موجودی کالا
    inventory_turnover_ratios = {}
    for year in years:
        cogs = cost_of_goods_sold.get(year)
        inventory = ending_inventory.get(year)

        if (
                cogs is None
                or inventory is None
                or inventory == 0
        ):
            pass
        else:
            inventory_turnover_ratios[year] = cogs / inventory

    return inventory_turnover_ratios


def calculate_inventory_in_sales_days(years, company):
    # دریافت نسبت گردش موجودی کالا
    inventory_turnover_ratios = calculate_inventory_turnover_ratio(years, company)
    if not inventory_turnover_ratios:
        print("Error: Could not find inventory turnover ratio data.")
        return None

    # محاسبه متوسط دوره گردش موجودی
    inventory_in_sales_days = {}
    for year in years:
        turnover_ratio = inventory_turnover_ratios.get(year)

        if turnover_ratio is None or turnover_ratio == 0:
            pass
        else:
            inventory_in_sales_days[year] = 365 / turnover_ratio

    return inventory_in_sales_days


def calculate_receivables_turnover_ratio(years, company):
    # دریافت فروش
    sales = find_by_row_years("فروش", years, company)
    if not sales:
        print("Error: Could not find sales data.")
        return None

    # دریافت حساب‌های دریافتنی
    receivables = find_by_row_years("حساب های دریافتنی", years, company)
    if not receivables:
        print("Error: Could not find receivables data.")
        return None

    # محاسبه نسبت گردش حساب‌های دریافتنی
    receivables_turnover_ratios = {}
    for year in years:
        sale = sales.get(year)
        receivable = receivables.get(year)

        if (
                sale is None
                or receivable is None
                or receivable == 0
        ):
            pass
        else:
            receivables_turnover_ratios[year] = sale / receivable

    return receivables_turnover_ratios


def calculate_average_collection_period(years, company):
    # دریافت نسبت گردش حساب‌های دریافتنی
    receivables_turnover_ratios = calculate_receivables_turnover_ratio(years, company)
    if not receivables_turnover_ratios:
        print("Error: Could not find receivables turnover ratio data.")
        return None

    # محاسبه متوسط دوره وصول مطالبات
    average_collection_period = {}
    for year in years:
        turnover_ratio = receivables_turnover_ratios.get(year)

        if turnover_ratio is None or turnover_ratio == 0:
            pass
        else:
            average_collection_period[year] = 365 / turnover_ratio

    return average_collection_period


def calculate_nwc_turnover_ratio(years, company):
    # دریافت فروش
    sales = find_by_row_years("فروش", years, company)
    if not sales:
        print("Error: Could not find sales data.")
        return None

    # دریافت سرمایه در گردش خالص (NWC)
    net_working_capital = find_by_row_years("سرمایه در گردش خالص", years, company)
    if not net_working_capital:
        print("Error: Could not find net working capital data.")
        return None

    # محاسبه نسبت گردش سرمایه در گردش خالص
    nwc_turnover_ratios = {}
    for year in years:
        sale = sales.get(year)
        nwc = net_working_capital.get(year)

        if (
                sale is None
                or nwc is None
                or nwc == 0
        ):
            pass
        else:
            nwc_turnover_ratios[year] = sale / nwc

    return nwc_turnover_ratios


def calculate_fixed_assets_turnover_ratio(years, company):
    # دریافت فروش
    sales = find_by_row_years("فروش", years, company)
    if not sales:
        print("Error: Could not find sales data.")
        return None

    # دریافت خالص دارایی‌های ثابت
    net_fixed_assets = find_by_row_years("خالص دارایی های ثابت", years, company)
    if not net_fixed_assets:
        print("Error: Could not find net fixed assets data.")
        return None

    # محاسبه نسبت گردش دارایی‌های ثابت
    fixed_assets_turnover_ratios = {}
    for year in years:
        sale = sales.get(year)
        net_assets = net_fixed_assets.get(year)

        if (
                sale is None
                or net_assets is None
                or net_assets == 0
        ):
            pass
        else:
            fixed_assets_turnover_ratios[year] = sale / net_assets

    return fixed_assets_turnover_ratios


def calculate_total_assets_turnover_ratio(years, company):
    # دریافت فروش
    sales = find_by_row_years("فروش", years, company)
    if not sales:
        print("Error: Could not find sales data.")
        return None

    # دریافت مجموع دارایی‌ها
    total_assets = find_by_row_years("مجموع دارایی ها", years, company)
    if not total_assets:
        print("Error: Could not find total assets data.")
        return None

    # محاسبه نسبت گردش دارایی‌های کل
    total_assets_turnover_ratios = {}
    for year in years:
        sale = sales.get(year)
        total_asset = total_assets.get(year)

        if (
                sale is None
                or total_asset is None
                or total_asset == 0
        ):
            pass
        else:
            total_assets_turnover_ratios[year] = sale / total_asset

    return total_assets_turnover_ratios


def calculate_profit_margin_ratio(years, company):
    # دریافت سود خالص
    net_profit = find_by_row_years("سود خالص", years, company)
    if not net_profit:
        print("Error: Could not find net profit data.")
        return None

    # دریافت فروش
    sales = find_by_row_years("فروش", years, company)
    if not sales:
        print("Error: Could not find sales data.")
        return None

    # محاسبه نسبت حاشیه سود
    profit_margin_ratios = {}
    for year in years:
        profit = net_profit.get(year)
        sale = sales.get(year)

        if (
                profit is None
                or sale is None
                or sale == 0
        ):
            pass
        else:
            profit_margin_ratios[year] = profit / sale

    return profit_margin_ratios


def calculate_roa_ratio(years, company):
    # دریافت سود خالص
    net_profit = find_by_row_years("سود خالص", years, company)
    if not net_profit:
        print("Error: Could not find net profit data.")
        return None

    # دریافت مجموع دارایی‌ها
    total_assets = find_by_row_years("مجموع دارایی ها", years, company)
    if not total_assets:
        print("Error: Could not find total assets data.")
        return None

    # محاسبه نرخ بازده دارایی‌ها
    roa_ratios = {}
    for year in years:
        profit = net_profit.get(year)
        total_asset = total_assets.get(year)

        if (
                profit is None
                or total_asset is None
                or total_asset == 0
        ):
            pass
        else:
            roa_ratios[year] = profit / total_asset

    return roa_ratios


def calculate_roe_ratio(years, company):
    # دریافت سود خالص
    net_profit = find_by_row_years("سود خالص", years, company)
    if not net_profit:
        print("Error: Could not find net profit data.")
        return None

    # دریافت حقوق صاحبان سهام
    shareholders_equity = find_by_row_years("حقوق صاحبان سهام", years, company)
    if not shareholders_equity:
        print("Error: Could not find shareholders equity data.")
        return None

    # محاسبه نرخ بازده حقوق صاحبان سهام
    roe_ratios = {}
    for year in years:
        profit = net_profit.get(year)
        equity = shareholders_equity.get(year)

        if (
                profit is None
                or equity is None
                or equity == 0
        ):
            pass
        else:
            roe_ratios[year] = profit / equity

    return roe_ratios


def calculate_ep_ratio(years, company):
    # دریافت قیمت هر سهم
    stock_price = find_by_row_years("قیمت هر سهم", years, company)
    if not stock_price:
        print("Error: Could not find stock price data.")
        return None

    # دریافت درآمد هر سهم
    earnings_per_share = find_by_row_years("درآمد هر سهم", years, company)
    if not earnings_per_share:
        print("Error: Could not find earnings per share data.")
        return None

    # محاسبه ضریب قیمت به درآمد هر سهم
    ep_ratios = {}
    for year in years:
        price = stock_price.get(year)
        earnings = earnings_per_share.get(year)

        if (
                price is None
                or earnings is None
                or earnings == 0
        ):
            pass
        else:
            ep_ratios[year] = price / earnings

    return ep_ratios


def calculate_mb_ratio(years, company):
    # دریافت ارزش بازار هر سهم
    market_value_per_share = find_by_row_years("ارزش بازار هر سهم", years, company)
    if not market_value_per_share:
        print("Error: Could not find market value per share data.")
        return None

    # دریافت ارزش دفتری هر سهم
    book_value_per_share = find_by_row_years("ارزش دفتری هر سهم", years, company)
    if not book_value_per_share:
        print("Error: Could not find book value per share data.")
        return None

    # محاسبه نسبت ارزش بازار به ارزش دفتری هر سهم
    mb_ratios = {}
    for year in years:
        market_value = market_value_per_share.get(year)
        book_value = book_value_per_share.get(year)

        if (
                market_value is None
                or book_value is None
                or book_value == 0
        ):
            pass
        else:
            mb_ratios[year] = market_value / book_value

    return mb_ratios
