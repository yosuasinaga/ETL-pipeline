import unittest
from unittest.mock import patch, Mock
from utils.extract import extract_all  # Pastikan fungsi ini sesuai dengan implementasi Anda

class TestExtract(unittest.TestCase):

    @patch("utils.extract.requests.get")
    def test_extract_returns_data(self, mock_get):
        """
        Menguji apakah fungsi extract_all mengembalikan data yang valid.
        """
        # Membuat konten HTML dummy untuk pengujian
        html_content = """
        <html>
            <body>
                <div class="product-details">
                    <h3 class="product-title">Test Product</h3>
                    <div class="price-container">
                        <span class="price">$10.00</span>
                    </div>
                    <p>Rating: ⭐ 4.5 / 5</p>
                    <p>5 Colors</p>
                    <p>Size: M</p>
                    <p>Gender: Unisex</p>
                </div>
            </body>
        </html>
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = html_content
        mock_get.return_value = mock_response

        # Panggil extract_all untuk mengambil data
        data = extract_all(1)  # Ambil hanya 1 halaman

        # Uji apakah data yang dikembalikan adalah list
        self.assertIsInstance(data, list)  # Memastikan data berupa list
        self.assertGreater(len(data), 0)  # Pastikan data tidak kosong
        self.assertIn('Title', data[0])   # Pastikan field "Title" ada pada setiap data
        self.assertIn('Price', data[0])   # Pastikan field "Price" ada pada setiap data
        self.assertIn('Rating', data[0])  # Pastikan field "Rating" ada pada setiap data
        self.assertIn('Colors', data[0])  # Pastikan field "Colors" ada pada setiap data
        self.assertIn('Size', data[0])    # Pastikan field "Size" ada pada setiap data
        self.assertIn('Gender', data[0])  # Pastikan field "Gender" ada pada setiap data

if __name__ == '__main__':
    unittest.main()
