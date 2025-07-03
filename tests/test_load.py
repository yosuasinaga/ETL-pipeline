import unittest
from unittest.mock import patch, Mock
import pandas as pd
from utils.load import save_to_csv, save_to_google_sheets

class TestLoad(unittest.TestCase):

    @patch("utils.load.service_account.Credentials.from_service_account_file")
    @patch("utils.load.build")
    def test_save_to_google_sheets(self, mock_build, mock_credentials):
        mock_service = Mock()
        mock_sheet = Mock()
        mock_service.spreadsheets.return_value = mock_sheet
        mock_build.return_value = mock_service

        df = pd.DataFrame({
            "Title": ["Product A"],
            "Price": [16000.0],
            "Rating": [4.5],
            "Colors": [5],
            "Size": ["M"],
            "Gender": ["Male"],
            "timestamp": ["2024-04-26 12:00:00"]
        })

        save_to_google_sheets(
            df, 
            spreadsheet_id="fake_spreadsheet_id", 
            sheet_name="Sheet1", 
            credentials_path="fake_credentials.json"
        )

        mock_sheet.values().update.assert_called()  # Memastikan panggilan untuk update sheet dilakukan

if __name__ == "__main__":
    unittest.main()
