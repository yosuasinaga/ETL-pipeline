import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
}

def extract_price(product_soup):
    try:
        # Cek apakah ada <div class="price-container">
        price_container = product_soup.find("div", class_="price-container")
        if price_container:
            price_text = price_container.find("span", class_="price").text.strip()
            if price_text.startswith("$"):
                return float(price_text.replace("$", "").replace(",", ""))
        else:
            # Cek apakah ada <p class="price">Price Unavailable</p> 
            p_price = product_soup.find("p", class_="price")
            if p_price and "Price Unavailable" in p_price.text:
                return None
    except Exception as e:
        print(f"Error extracting price: {e}")
    return None

def extract_page(page):
    """
    Mengekstrak data produk dari halaman URL yang diberikan.
    
    Args:
        page (int): Nomor halaman yang ingin diambil datanya.
    
    Returns:
        List: Daftar produk yang berhasil diekstrak dari halaman.
    """
    url = f"https://fashion-studio.dicoding.dev/page{page}" if page != 1 else "https://fashion-studio.dicoding.dev/"
    
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    product_elements = soup.find_all("div", class_="product-details")

    data = []

    for product in product_elements:
        try:
            title = product.find("h3", class_="product-title").text.strip()
            price = extract_price(product)

            p_tags = product.find_all("p")
            rating_text = next((p.text.strip() for p in p_tags if "Rating:" in p.text), "Rating: Not Rated")
            colors_text = next((p.text.strip() for p in p_tags if "Colors" in p.text), "0 Colors")
            size_text = next((p.text.strip() for p in p_tags if "Size:" in p.text), "Size: Unknown")
            gender_text = next((p.text.strip() for p in p_tags if "Gender:" in p.text), "Gender: Unknown")

            data.append({
                "Title": title,
                "Price": price,
                "Rating": rating_text,
                "Colors": colors_text,
                "Size": size_text,
                "Gender": gender_text
            })
        except Exception as e:
            print(f"Error extracting product: {e}")
            continue

    return data

def extract_all(max_page=50):
    """
    Mengekstrak data produk dari beberapa halaman.
    
    Args:
        max_page (int): Jumlah halaman maksimal yang akan diekstrak.
    
    Returns:
        List: Daftar produk dari semua halaman.
    """
    all_data = []
    for page in range(1, max_page + 1):
        all_data.extend(extract_page(page))
    return all_data
