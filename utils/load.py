import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account

def save_to_csv(df, path="products.csv"):
    """
    Menyimpan DataFrame ke file CSV.

    Args:
        df (pandas.DataFrame): Data yang akan disimpan.
        path (str): Nama file CSV yang akan digunakan untuk menyimpan data.
    """
    df.to_csv(path, index=False)
    print(f"Data berhasil disimpan ke {path}")

def save_to_google_sheets(df, spreadsheet_id, sheet_name, credentials_path):
    """
    Menyimpan DataFrame ke Google Sheets.

    Args:
        df (pandas.DataFrame): Data yang akan disimpan.
        spreadsheet_id (str): ID spreadsheet Google Sheets.
        sheet_name (str): Nama sheet yang ingin diupdate.
        credentials_path (str): Path ke file kredensial Google Sheets API.
    """
    # Menangani nilai NaN atau Null
    df = df.fillna('')

    # Menangani karakter-karakter tidak valid seperti newline, tab, dll.
    df = df.applymap(str).replace({'\n': ' ', '\r': ' ', '\t': ' '}, regex=True)

    # Mengautentikasi menggunakan service account
    creds = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()

    # Menyiapkan data untuk disimpan ke Sheets
    body = {
        "values": [df.columns.tolist()] + df.values.tolist()  # Menambahkan header dan data
    }

    # Mengupdate Google Sheets dengan data
    sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=sheet_name,
        valueInputOption="RAW",
        body=body
    ).execute()

    print(f"Data berhasil disimpan ke Google Sheets ({sheet_name})")
