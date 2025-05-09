import streamlit as st

# Set up page
st.set_page_config(page_title="Simulasi IoT: Penyiraman Tanaman Otomatis", layout="centered")

st.title("🌱 Simulasi Penyiraman Tanaman Otomatis dengan IoT")
st.markdown("""
Sistem ini menggunakan **sensor kelembaban tanah** untuk memutuskan apakah tanaman perlu disiram atau tidak.
""")

# Input simulasi kelembaban tanah
soil_moisture = st.slider("Tingkat Kelembaban Tanah (%)", 0, 100, 50)

# Simulasi logika penyiraman otomatis
if soil_moisture < 30:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Watering_can_icon.svg/1200px-Watering_can_icon.svg.png", width=100)
    st.success("💧 Sistem Penyiraman AKTIF karena kelembaban tanah rendah.")
else:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/04/Watering_can_icon_no_watering.svg", width=100)
    st.info("🌿 Tanaman cukup lembab, sistem penyiraman MATI.")

# Penjelasan singkat
st.markdown("""
---
### 🤔 Apa itu IoT?
**Internet of Things (IoT)** memungkinkan perangkat (seperti sensor kelembaban tanah) untuk terhubung dan berinteraksi dengan perangkat lain secara otomatis. Dalam hal ini, sensor mengirimkan data tentang kelembaban tanah, dan sistem otomatis mengontrol penyiraman tanaman berdasarkan data tersebut.
""")
