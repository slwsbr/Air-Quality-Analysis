import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# --- Sidebar Styling ---
st.sidebar.title("⚙️ Dashboard")
st.sidebar.write("Merupakan hasil analisis data kualitas udara di Kota Dingling, Guanyuan, dan Gucheng  ")
st.sidebar.markdown("---")

# Upload file CSV
df1 = pd.read_csv("data/air_quality (2).csv")
df2 = pd.read_csv("data/air_quality (3).csv")
df3 = pd.read_csv("data/air_quality (1).csv")

# Pilih tampilan awal dengan ikon
tab = st.sidebar.selectbox("📊 Pilih Analisis", [
    "📄 Data yang digunakan", 
    "📈 Tren Tahunan Polutant", 
    "📊 Bar Plot", 
    "🌡️ Heatmap"
])

st.sidebar.markdown("---")

# --- Tampilkan Data yang digunakan ---
if tab == "📄 Data yang digunakan":
    st.title("📄 Dataset Kualitas Udara di Kota Dingling, Guanyuan, dan Gucheng")
    st.write("Berikut adalah data yang digunakan untuk analisis data.")
    st.subheader("Data Polutant Udara per Jam di Kota Dingling, Guanyuan, dan Gucheng ")
    st.dataframe(df3.head(), use_container_width=True)
    st.subheader("Data Rata-Rata Polutant Udara per Tahun di Kota Dingling, Guanyuan, dan Gucheng ")
    st.dataframe(df1.head(), use_container_width=True)
    st.subheader("Data Persentase Polutant yang Overlimit dari Batas WHO di Kota Dingling, Guanyuan, dan Gucheng")
    st.dataframe(df2.head(), use_container_width=True)

# --- Tren Tahunan ---
if tab == "📈 Tren Tahunan Polutant":
    cities = df1["station"].unique()
    
    parameters = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
    selected_param = st.sidebar.selectbox("📌 Pilih Parameter", parameters)
    st.title("📈 Tren Tahunan Polutan")

    city_styles = {
        "Dingling": {"marker": "o", "linestyle": "-", "color": "#1f77b4"},
        "Gucheng": {"marker": "^", "linestyle": "--", "color": "#ff7f0e"},
        "Guanyuan": {"marker": "s", "linestyle": "-.", "color": "#2ca02c"},
    }
    
    years = df1["year"].unique()
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    for city, style in city_styles.items():
        city_data = df1[df1["station"] == city]
        ax1.plot(city_data["year"], city_data[selected_param], label=city, **style)
    ax1.set_title(f"Trend {selected_param}")
    ax1.set_xlabel("Tahun")
    ax1.set_ylabel("Rata-rata")
    ax1.legend()
    ax1.grid(True, linestyle="--", alpha=0.3)
    st.pyplot(fig1)

    # Buat dictionary analisis untuk tiap parameter
    analysis_text = {
        "PM2.5": """
**PM2.5:**
- Gucheng cenderung memiliki nilai PM2.5 terttinggi dan pada tahun-tahun akhir meningkat secara signifikan.
- Guanyuan berada di kisaran menengah tetapi pada tahun akhir menunjukkan tren naik.
- Dingling cenderung paling rendah, meskipun pada tengah periode sempat naik-turun.
        """,
        "PM10": """
**PM10:**
- Gucheng konsisten menempati posisi tertinggi dan mencapai puncak saat pertengahan periode, lalu turun dan naik kembali.
- Guanyuan berada di posisi menengah, sempat ada tren turun lalu meningkat lagi di akhir.
- Dingling menjadi yang paling rendah dan cenderung terus menurun.
        """,
        "SO2": """
**SO2:**
- Guanyuan secara umum paling tinggi. Sempat terjadi penurunan yang besar, tetapi di tahun terakhir kembali meningkat.
- Gucheng berada di posisi menengah, turun drastis di satu periode, lalu naik lagi.
- Dingling cenderung paling rendah, meski naik-turun.
        """,
        "NO2": """
**NO2:**
- Guanyuan memiliki nilai NO2 yang tinggi, dengan puncak di sekitar 2013-2014 lalu menurun di 2015, kemudian naik hingga 2017.
- Gucheng memiliki pola yang sama dengan Guanyuan.
- Dingling memiliki nilai terendah di antara ketiga kota, cenderung stabil, sempat menurun dan kembali naik.
        """,
        "CO": """
**CO:**
- Guanyuan mulai dengan nilai yang cukup tinggi tetapi akhirnya turun dan kembali naik di 2017.
- Gucheng memiliki puncak di tahun awal, lalu turun di 2016 dan kembali naik di 2017.
- Dingling turun pada tahun 2014-2016 dan kembali naik di 2017.
        """,
        "O3": """
**O3:**
- Guanyuan mulai di kisaran 50, lalu naik di tahun 2015 dan perlahan turun di 2017.
- Gucheng mulai di angka 55, stabil hingga 2016 dan menurun drastis di 2017.
- Dingling tertinggi hingga 2014, lalu menurun secara bertahap di 2017.
        """
    }

    # Tampilkan analisis yang sesuai dengan parameter yang dipilih
    st.markdown(analysis_text[selected_param])


# --- Bar Plot: Perbandingan Over Limit ---
if tab == "📊 Bar Plot":
    st.title("📊 Perbandingan Nilai Over Limit Polutan per Stasiun")
    pollutants = ['PM2.5_overlimit', 'PM10_overlimit', 'SO2_overlimit', 'CO_overlimit', 'O3_overlimit', 'NO2_overlimit']
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    x = np.arange(len(pollutants))
    width = 0.25

    for i, city in enumerate(df2["station"].unique()):
        city_data = df2[df2["station"] == city]
        mean_values = city_data[pollutants].mean().values  
        if len(mean_values) == len(x):  
            ax2.bar(x + i * width, mean_values, width=width, label=city)
        else:
            st.warning(f"Data di {city} tidak sesuai untuk plotting bar chart.")
    
    ax2.set_xticks(x + width)
    ax2.set_xticklabels(pollutants, rotation=45)
    ax2.set_ylabel("Over Limit Value")
    ax2.legend()
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig2)

# --- Heatmap: Persentase Over Limit ---
if tab == "🌡️ Heatmap":
    st.title("🌡️ Heatmap Persentase Over Limit per Stasiun")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    pollutants = ['PM2.5_overlimit', 'PM10_overlimit', 'SO2_overlimit', 'CO_overlimit', 'O3_overlimit', 'NO2_overlimit']
    pivot_data = df2.pivot_table(index="station", values=pollutants, aggfunc='mean')
    sns.heatmap(pivot_data, annot=True, cmap="YlGnBu", linewidths=0.5)
    ax3.set_title("Persentase Over Limit per Stasiun")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    st.pyplot(fig3)
    st.markdown("""
    1. **Dingling**  
    Memiliki PM2.5, PM10, NO2, dan SO2 yang lebih rendah dibandingkan kota lain, tetapi persentase PM2.5-nya masih tinggi sekitar 84%. Kadar O3 sedikit lebih tinggi (18%) dari kota lain, hal ini kemungkinan dipengaruhi oleh kondisi meteorologi atau tingkat emisi prekursor.

    2. **Guanyuan**  
    Memiliki PM2.5 dan PM10 yang sangat tinggi (93% dan 81%). Memiliki NO2 paling tinggi (82%) serta SO2 tertinggi (12%). Hal ini membuat Guanyuan memiliki kualitas udara yang kurang sehat dengan adanya polusi yang pekat.

    3. **Gucheng**  
    Memiliki PM2.5 dan PM10 yang sangat tinggi (93% dan 87%). Memiliki NO2 yang tinggi (76%). Hal ini membuat Gucheng memiliki polusi udara yang cukup tinggi dan kualitas udara yang kurang sehat.
    """)
