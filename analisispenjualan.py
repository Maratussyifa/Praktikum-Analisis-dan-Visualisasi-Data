import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# membaca data CSV
df = pd.read_csv("data_praktikum_analisis_data - data_praktikum_analisis_data.csv")

# lihat 5 data pertama
print(df.head())

# cek tipe data
print(df.info())

# cek data kosong
print(df.isnull().sum())


# ==============================
# DATA CLEANING
# ==============================

# ubah kolom tanggal menjadi datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# hapus data Total_Sales yang kosong
df = df.dropna(subset=['Total_Sales'])

# hapus harga yang tidak valid
df = df[df['Price_Per_Unit'] > 0]


# ==============================
# ANALISIS TREN PENJUALAN
# ==============================

df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')

plt.title("Tren Penjualan Bulanan")
plt.xticks(rotation=45)

plt.show()


# ==============================
# ANALISIS KORELASI
# ==============================

correlation = df[['Total_Sales','Ad_Budget','Quantity']].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')

plt.title("Peta Korelasi Variabel")

plt.show()


# ==============================
# 1. IDENTIFIKASI PRODUK UNDERPERFORMER
# ==============================

avg_price = df['Price_Per_Unit'].mean()

underperformer = df[df['Price_Per_Unit'] > avg_price]

print("\nProduk harga tinggi namun quantity kecil:")
print(underperformer[['Price_Per_Unit','Quantity']].sort_values(by='Quantity').head())

plt.figure(figsize=(8,5))
plt.scatter(df['Price_Per_Unit'], df['Quantity'])

plt.xlabel("Price Per Unit")
plt.ylabel("Quantity")
plt.title("Produk Mahal vs Jumlah Terjual")

plt.show()


# ==============================
# 2. SEGMENTASI PELANGGAN (RFM ANALYSIS)
# ==============================

snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})

rfm.columns = ['Recency','Frequency','Monetary']

print("\nData RFM:")
print(rfm.head())


# ==============================
# 5. RFM SCORING (LANJUTAN)
# ==============================

rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

rfm['RFM_Group'] = rfm.R_Score.astype(str) + rfm.F_Score.astype(str) + rfm.M_Score.astype(str)

print("\nRFM Scoring:")
print(rfm.head())


# ==============================
# 3. ANALISIS KONTRIBUSI KATEGORI
# ==============================

category = df.groupby('Product_Category').agg({
    'Total_Sales':'sum',
    'Ad_Budget':'sum'
})

category['Efficiency'] = category['Total_Sales'] / category['Ad_Budget']

category = category.sort_values('Efficiency')

plt.figure(figsize=(8,5))
category['Efficiency'].plot(kind='barh')

plt.title("Efisiensi Kategori Produk")

plt.show()


# ==============================
# 4. UJI HIPOTESIS IKLAN
# ==============================

median_ads = df['Ad_Budget'].median()

high_ads = df[df['Ad_Budget'] > median_ads]
low_ads = df[df['Ad_Budget'] <= median_ads]

print("\nRata-rata penjualan iklan tinggi:", high_ads['Total_Sales'].mean())
print("Rata-rata penjualan iklan rendah:", low_ads['Total_Sales'].mean())


# ==============================
# 6. REGRESI LINEAR SEDERHANA
# ==============================

X = df[['Ad_Budget']]
y = df['Total_Sales']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

print("\nKoefisien Iklan:", model.coef_[0])
print("Akurasi Model (R2 Score):", model.score(X_test, y_test))