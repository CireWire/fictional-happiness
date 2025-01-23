import pandas as pd

def csv_to_excel(csv_file, excel_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Write the dataframe to an excel file
    df.to_excel(excel_file, index=False, engine='openpyxl')

    print(f"File converted successfully and saved as {excel_file}")


# Example usage
csv_file = "data.csv" # File to be converted
excel_file = "data.xlsx" # File to be saved
csv_to_excel(csv_file, excel_file)
