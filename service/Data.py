import pandas as pd
from matplotlib import pyplot as plt


def find_by_row_year(row, year, company):
    try:
        df = pd.read_csv(company, encoding='utf-8')
        financial_facilities_row = df[df['عنوان'].str.contains(row.strip(), na=False, regex=False)]
        if financial_facilities_row.empty:
            return None

        if year in df.columns:
            value = financial_facilities_row[year].values[0]
            return value if pd.notna(value) else None
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def find_by_row_years(row, years, company):
    try:
        df = pd.read_csv(company, encoding='utf-8')
        financial_facilities_row = df[df['عنوان'].str.contains(row.strip(), na=False, regex=False)]
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
    except Exception as e:
        print(f"Error: {e}")
        return None


def plot_row_years(row, years, company):
    data = find_by_row_years(row, years, company)

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
