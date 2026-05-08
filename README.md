📊 Analisis Data Penjualan

Proyek ini merupakan praktikum analisis data menggunakan Python untuk memahami pola penjualan, perilaku pelanggan, serta efektivitas anggaran iklan berdasarkan dataset transaksi penjualan.

Analisis dilakukan menggunakan library Python seperti:

pandas → pengolahan data
matplotlib → visualisasi data
seaborn → visualisasi heatmap
scikit-learn → analisis regresi

1️⃣ Business Question
Analisis ini bertujuan menjawab beberapa pertanyaan bisnis berikut:
Produk apa yang memiliki harga tinggi tetapi volume penjualan rendah (underperformer)?
Bagaimana segmentasi pelanggan berdasarkan metode RFM Analysis?
Kategori produk mana yang memiliki efisiensi terbaik antara biaya iklan dan pendapatan?
Apakah peningkatan Ad_Budget benar-benar meningkatkan Total_Sales?
Bagaimana tren penjualan bulanan selama periode data?

Pertanyaan ini membantu perusahaan memahami strategi penjualan yang lebih efektif.

2️⃣ Data Wrangling
Sebelum melakukan analisis, data terlebih dahulu dibersihkan dengan langkah berikut:

Data Cleaning
Mengubah kolom Order_Date menjadi format datetime
Menghapus data yang memiliki Total_Sales kosong
Menghapus data dengan Price_Per_Unit ≤ 0 karena dianggap tidak valid
Feature Engineering
Menambahkan kolom Month untuk menganalisis tren penjualan bulanan

Tujuan dari tahap ini adalah memastikan data bersih, konsisten, dan siap dianalisis.

3️⃣ Insights
📈 Tren Penjualan Bulanan
Analisis tren menunjukkan bahwa penjualan mengalami fluktuasi sepanjang tahun dengan puncak penjualan pada bulan Agustus.
Hal ini menunjukkan adanya kemungkinan faktor seperti:

promo
musim belanja
peningkatan permintaan pasar
🔥 Korelasi Antar Variabel
<img width="1504" height="853" alt="image" src="https://github.com/user-attachments/assets/9002c4b2-5a82-4de7-8a20-7f172b3c1f34" />


Heatmap korelasi menunjukkan hubungan antar variabel:
Variabel	Korelasi
Total_Sales vs Quantity	0.64 (cukup kuat)
Total_Sales vs Ad_Budget	0.055 (sangat lemah)
Ad_Budget vs Quantity	0.12 (lemah)
<img width="964" height="823" alt="image" src="https://github.com/user-attachments/assets/1b327c71-7d83-4fb4-8a45-aa68b9b955c2" />


Insight:
Jumlah produk yang terjual memiliki pengaruh yang lebih besar terhadap total penjualan dibandingkan anggaran iklan.

💰 Produk Underperformer
<img width="1204" height="852" alt="image" src="https://github.com/user-attachments/assets/9e529260-bac7-4584-a057-41a66d001531" />

Scatter plot menunjukkan beberapa produk dengan:
Price_Per_Unit tinggi
Quantity rendah

Produk tersebut dapat dikategorikan sebagai produk underperformer, karena memiliki nilai produk tinggi tetapi jarang terjual.

🛍 Efisiensi Kategori Produk
<img width="1204" height="853" alt="image" src="https://github.com/user-attachments/assets/4e89bcf4-3a39-4581-a5b0-041c16e5ca9d" />


Analisis efisiensi kategori menunjukkan:

Kategori	Efisiensi
Electronics	Paling efisien
Books	Efisien
Fashion	Sedang
Home Decor	Kurang efisien
Gadget	Paling rendah

Artinya kategori Electronics memberikan pendapatan terbesar dibandingkan biaya iklan.

👥 Segmentasi Pelanggan (RFM Analysis)

RFM Analysis digunakan untuk mengelompokkan pelanggan berdasarkan:

Recency → kapan terakhir belanja
Frequency → seberapa sering bertransaksi
Monetary → total uang yang dihabiskan

Metode ini membantu perusahaan mengidentifikasi:

pelanggan loyal
pelanggan potensial
pelanggan yang mulai tidak aktif
📉 Analisis Regresi Linear

Regresi linear digunakan untuk menganalisis hubungan antara:

Ad_Budget → Total_Sales

Model ini membantu memprediksi apakah peningkatan anggaran iklan akan berdampak pada peningkatan penjualan.

Hasil analisis menunjukkan bahwa hubungan antara anggaran iklan dan penjualan tidak terlalu kuat.

4️⃣ Recommendation

Berdasarkan hasil analisis data, beberapa rekomendasi yang dapat diberikan adalah:

1️⃣ Evaluasi Produk Mahal

Produk dengan harga tinggi tetapi volume penjualan rendah perlu dievaluasi, misalnya dengan:
menyesuaikan harga
memberikan diskon
meningkatkan promosi

2️⃣ Fokus pada Kategori Efisien
Kategori Electronics memiliki efisiensi tertinggi sehingga perusahaan dapat meningkatkan investasi pemasaran pada kategori ini.

3️⃣ Optimasi Anggaran Iklan
Karena korelasi antara Ad_Budget dan Total_Sales lemah, perusahaan perlu mengevaluasi strategi iklan agar lebih efektif.

4️⃣ Program Loyalitas Pelanggan
Gunakan hasil RFM Analysis untuk memberikan:
voucher loyalitas
promo khusus pelanggan aktif
program membership

📌 Kesimpulan
Analisis data menunjukkan bahwa faktor utama yang mempengaruhi penjualan adalah jumlah produk yang terjual, bukan hanya anggaran iklan. Selain itu, kategori produk memiliki tingkat efisiensi yang berbeda sehingga perusahaan perlu memfokuskan strategi pada kategori yang paling menguntungkan.
