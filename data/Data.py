import pandas as pd

def get_company():
    companies = {"ذوب", "شبندر", "فولاد"}
    print(" ".join(companies))

    company = input("\U0001F4C3 \033[1;36menter company name: \033[0m").strip()
    if company == "ذوب":
        return "data/ذوب.csv"
    if company == "شبندر":
        return "data/شبندر.csv"
    if company == "فولاد":
        return "data/فولاد.csv"


def find_by_row_year(row, year, company):
    df = pd.read_csv(company, encoding='utf-8')
    financial_facilities_row = df[df['عنوان'].str.contains(row, na=False)]
    if financial_facilities_row.empty:
        return None
    else:
        return financial_facilities_row[year].values[0]


def find_by_row_years(row, years, company):
    df = pd.read_csv(company, encoding='utf-8')
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