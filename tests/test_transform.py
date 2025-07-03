import unittest
import pandas as pd
from utils.transform import transform_data  # Pastikan fungsi ini sesuai dengan implementasi Anda

class TestTransform(unittest.TestCase):

    def test_transform_data_success(self):
        """
        Menguji apakah kolom 'rating' dan 'price' ditransformasi dengan benar.
        """
        # Menyiapkan data dummy
        raw_data = [
            {
                "Title": "Test Product",
                "Price": "20.0",  # Harga dalam string
                "Rating": "Rating: ⭐ 4.0 / 5",
                "Colors": "3 Colors",
                "Size": "Size: L",
                "Gender": "Gender: Male"
            }
        ]

        # Melakukan transformasi pada data dummy
        transformed = transform_data(raw_data)

        # Memastikan bahwa kolom 'Price' diubah menjadi float
        self.assertIsInstance(transformed['Price'].iloc[0], float, "Harga tidak diubah menjadi float")
        self.assertEqual(transformed['Price'].iloc[0], 320000.0, "Harga tidak sesuai dengan konversi ke rupiah")

        # Memastikan bahwa kolom 'Rating' diubah menjadi float
        self.assertEqual(transformed['Rating'].iloc[0], 4.0, "Rating tidak diubah menjadi angka float")

        # Memastikan kolom-kolom lainnya ada
        self.assertEqual(transformed['Title'].iloc[0], "Test Product")
        self.assertEqual(transformed['Colors'].iloc[0], 3)
        self.assertEqual(transformed['Size'].iloc[0], "L")
        self.assertEqual(transformed['Gender'].iloc[0], "Male")

    def test_transform_data_handle_invalid(self):
        """
        Menguji apakah data yang invalid (seperti harga atau rating tidak valid) ditangani dengan baik.
        """
        raw_data = [
            {
                "Title": "Unknown Product",
                "Price": None,
                "Rating": "Rating: Not Rated",
                "Colors": "0 Colors",
                "Size": "Size: Unknown",
                "Gender": "Gender: Unknown"
            }
        ]
        
        transformed = transform_data(raw_data)
        # Pastikan tidak ada data yang tersisa karena semua data dianggap invalid
        self.assertEqual(len(transformed), 0, "Data invalid tidak terhapus dengan benar")

if __name__ == "__main__":
    unittest.main()
