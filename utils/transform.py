import pandas as pd
from datetime import datetime

def transform_data(raw_data):
    """
    Melakukan transformasi data produk yang meliputi konversi harga, rating, dan penghapusan data tidak valid.
    
    Args:
        raw_data (list): Data mentah yang telah diekstrak dari website.
        
    Returns:
        pandas.DataFrame: Data yang telah ditransformasi dalam bentuk DataFrame.
    """
    # Konversi data mentah (list of dictionaries) ke DataFrame
    df = pd.DataFrame(raw_data)
    
    transformed = []
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for _, item in df.iterrows():
        try:
            title = item.get("Title", "").strip()
            price = item.get("Price", None)
            rating_raw = item.get("Rating", "")
            colors_raw = item.get("Colors", "0 Colors")
            size_raw = item.get("Size", "Size: Unknown")
            gender_raw = item.get("Gender", "Gender: Unknown")

            # Filter data invalid sebelum diproses
            if title in ["Unknown Product", None, ""]:
                continue
            if price is None:
                continue
            if rating_raw in ["Rating: Invalid Rating", "Rating: Not Rated"]:
                continue

            # Konversi harga ke rupiah
            price_rupiah = float(price) * 16000

            # Rating
            if "⭐" in rating_raw and "/" in rating_raw:
                rating_part = rating_raw.split("⭐")[1].split("/")[0].strip()
                rating = float(rating_part)
            else:
                rating = None

            if rating is None:
                continue

            colors = int(colors_raw.split()[0])
            size = size_raw.replace("Size:", "").strip()
            gender = gender_raw.replace("Gender:", "").strip()

            transformed.append({
                "Title": title,
                "Price": round(price_rupiah, 2),
                "Rating": rating,
                "Colors": colors,
                "Size": size,
                "Gender": gender,
                "timestamp": timestamp
            })

        except Exception as e:
            print(f"Error transforming data: {e}")
            continue

    # Mulai cleaning tahap akhir
    df = pd.DataFrame(transformed)
    
    if df.empty:
        return df
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    # Memastikan data biar valid
    invalid_titles = ["Unknown Product", None, ""]
    invalid_ratings = ["Invalid Rating", "Not Rated", None]
    invalid_prices = [None]

    df = df[~df["Title"].isin(invalid_titles)]
    df = df[~df["Rating"].isin(invalid_ratings)]
    df = df[~df["Price"].isin(invalid_prices)]

    # Set tipe data
    df = df.astype({
        "Title": "object",
        "Price": "float",
        "Rating": "float",
        "Colors": "int",
        "Size": "object",
        "Gender": "object",
        "timestamp": "object"
    })

    return df
