# Air-Quality-Analysis
Dashboard ini merupakan hasil analisis data kualitas udara di tiga kota, yaitu **Dingling**, **Guanyuan**, dan **Gucheng**. Analisis yang disediakan meliputi:

- **Data yang digunakan**: Menampilkan preview dari tiga dataset (data polutan per jam, data rata-rata polutan per tahun, dan data persentase polutan yang over limit menurut standar WHO).
- **Tren Tahunan Polutan**: Menampilkan grafik tren tahunan untuk masing-masing parameter polutan (PM2.5, PM10, SO2, NO2, CO, dan O3) berdasarkan data rata-rata per tahun.
  - Pengguna dapat memilih parameter yang ingin dianalisis melalui sidebar.
  - Setelah grafik ditampilkan, akan muncul analisis singkat yang menjelaskan tren untuk parameter yang dipilih.
- **Bar Plot**: Menampilkan perbandingan nilai over limit polutan per stasiun.
- **Heatmap**: Menampilkan heatmap persentase over limit per stasiun, disertai dengan penjelasan tentang karakteristik kualitas udara masing-masing kota.


### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run dashboard/dashboard_air.py
   ```
