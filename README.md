# ETL-pipeline

Proyek ETL (Extract, Transform, Load) berbasis Python yang dirancang untuk mengotomatisasi alur kerja data. Repositori ini menyediakan skrip dan utilitas untuk mengekstrak data dari berbagai sumber, mentransformasikan data sesuai kebutuhan analisis, dan memuatnya ke dalam tujuan akhir seperti basis data atau data warehouse.

## Fitur

- **Extract**: Mengambil data dari berbagai sumber (database, API, file, dll).
- **Transform**: Membersihkan, memanipulasi, dan membentuk ulang data sesuai logika bisnis.
- **Load**: Memasukkan data yang telah diproses ke dalam tujuan akhir.
- Desain modular dan mudah dikembangkan untuk menambah sumber data atau transformasi baru.
- Logging dan penanganan error untuk operasi yang andal.

## Struktur Proyek

```
etl-pipeline/
│
├── tests/ # Folder untuk pengujian unit
├── utils/ # Folder untuk fungsi utilitas
├── .gitignore # Mengabaikan file atau direktori tertentu dalam repositori
├── README.md # Deskripsi proyek
├── main.py # Skrip utama untuk pipeline ETL
├── products.csv # Dataset produk yang diproses
├── requirements.txt # Daftar dependensi proyek
└── submission.txt # Instruksi atau dokumentasi proyek
```

## Memulai

### Prasyarat

- Python 3.7+
- Disarankan: Membuat virtual environment

### Instalasi

Klon repositori:
```bash
git clone https://github.com/yosuasinaga/ETL-pipeline.git
cd ETL-pipeline
```

Instal dependensi:
```bash
pip install -r requirements.txt
```

### Konfigurasi

Edit file konfigurasi di direktori `config/` untuk menentukan sumber data, kredensial, dan pengaturan pipeline.

### Penggunaan

Untuk menjalankan pipeline ETL:
```bash
python main.py
```
Anda dapat menyesuaikan pipeline dengan memodifikasi atau menambah skrip pada direktori `extract/`, `transform/`, dan `load/`.
