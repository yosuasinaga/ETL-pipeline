from utils.extract import extract_all  
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets
import pandas as pd
import time

# URL website yang ingin di-scrape
URL = "https://fashion-studio.dicoding.dev"
NUM_PAGES = 50

# Path ke file JSON kredensial Google Sheets
CREDENTIALS_PATH = "google-sheets-api.json"
SPREADSHEET_ID = "1mOHCK7F3dwNojWfMTRzFrqs49Z_kCN8T-jfu2NfIlO4"
SHEET_NAME = "Sheet1"

def main():
    """
    Proses utama untuk mengekstrak, mentransformasi, dan menyimpan data produk ke CSV dan Google Sheets.
    """
    # Ekstrak data dari 50 halaman
    all_raw_data = extract_all(NUM_PAGES)  
    
    # Transformasi data yang sudah diambil
    transformed_data = transform_data(all_raw_data)

    # Simpan data yang telah ditransformasi ke file CSV
    df = pd.DataFrame(transformed_data)
    save_to_csv(df)  # Fungsi untuk menyimpan data ke CSV

    # Simpan data ke Google Sheets
    save_to_google_sheets(df, SPREADSHEET_ID, SHEET_NAME, CREDENTIALS_PATH)

    print("Proses selesai")

if __name__ == "__main__":
    main()
