from service.Data import *
from util.Help import *


def get_values_by_row_years():
    menu = print_tables()
    number = get_input_number()
    row = menu[number - 1]
    years = get_valid_years()
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    result = find_by_row_years(row, years, get_company())
    display_result(f"Results for '{row}' over years", result)


def print_tables():
    menu = [
        "درآمدهای عملياتی",
        "بهاى تمام شده درآمدهای عملياتی",
        "سود(زيان) ناخالص",
        "هزينه‏ هاى فروش، ادارى و عمومى",
        "ساير درآمدها",
        "ساير هزينه‌ها",
        "سود(زيان) عملياتى",
        "هزينه‏ هاى مالى",
        "ساير درآمدها و هزينه ‏هاى غيرعملياتى",
        "سود(زيان) عمليات در حال تداوم قبل از ماليات",
        "سال جاری",
        "سال‌های قبل",
        "سود(زيان) خالص عمليات در حال تداوم",
        "سود(زيان) خالص",
        "عملياتی (ريال)",
        "غيرعملياتی (ريال)",
        "ناشی از عمليات در حال تداوم",
        "ناشی از عمليات متوقف شده",
        "سود(زيان) پايه هر سهم",
        "سود (زيان) خالص هر سهم – ريال",
        "سرمايه",
        "دارايی های ثابت مشهود",
        "دارايی های نامشهود",
        "سرمايه‌گذاری های بلندمدت",
        "دريافتنی های بلندمدت",
        "ساير دارايی ها",
        "جمع دارايی های غيرجاری",
        "سفارشات و پيش‌پرداخت‌ها",
        "موجودی مواد و کالا",
        "دريافتنی های تجاری و ساير دريافتنی ها",
        "سرمايه‌گذاری های کوتاه‌مدت ",
        "موجودی نقد",
        "دارايی های نگهداری شده برای فروش",
        "جمع دارايی های جاری",
        "جمع دارایی ها",
        "سرمايه",
        "افزايش سرمايه در جريان",
        "صرف سهام",
        "صرف سهام خزانه",
        "اندوخته قانونی",
        "ساير اندوخته‌ها",
        "مازاد تجديدارزيابی دارايی ها",
        "تفاوت تسعير ارز عمليات خارجی",
        "سود(زيان) انباشته",
        "سهام خزانه",
        "جمع حقوق مالکانه",
        "پرداختنی های بلندمدت",
        "تسهيلات مالی بلندمدت",
        "ذخيره مزايای پايان خدمت کارکنان",
        "جمع بدهی های غيرجاری",
        "پرداختنی های تجاری و ساير پرداختنی ها",
        "ماليات پرداختنی",
        "سود سهام پرداختنی",
        "تسهيلات مالی",
        "ذخاير",
        "پيش‌دريافت‌ها",
        "بدهی های ‌مرتبط ‌با دارايی های نگهداری شده برای ‌فروش",
        "جمع بدهی های جاری",
        "جمع بدهی ها",
        "جمع حقوق مالکانه و بدهی ها",
        "استهلاک",
    ]
    max_width = max(len(item) for item in menu) + 10
    border = f"\u250c{''.ljust(max_width, '\u2500')}\u2510"
    separator = f"\u251c{''.ljust(max_width, '\u2500')}\u2524"
    footer = f"\u2514{''.ljust(max_width, '\u2500')}\u2518"

    print(border)
    print(
        f"| {f'\033[1;34m\u0644\u06cc\u0633\u062a \u06af\u0632\u06cc\u0646\u0647\u200c\u0647\u0627\033[0m'.center(max_width)} |")
    print(separator)
    for i, item in enumerate(menu, 1):
        index = f"\033[1;33m{i:2d}.\033[0m"
        print(f"| {index} {item.ljust(max_width - len(index) - 2)} |")
    print(footer)
    return menu


def plot_values_by_row_years():
    menu = print_tables()
    number = get_input_number()
    row = menu[number - 1]
    years = get_valid_years()
    if not years:
        print("\U0001F6AB \033[1;31mInvalid years input.\033[0m")
        return
    plot_row_years(row, years, get_company())


def get_input_number():
    while True:
        number = int(input("\U0001F4C3 \033[1;36mChoose an option: \033[0m").strip())
        if number not in range(1, 62):
            print("\033[1;31mInvalid input. Please choose valid option.\033[0m")
            continue
        else:
            return number
