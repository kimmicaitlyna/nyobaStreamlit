import streamlit as st

st.set_page_config(page_title="Simulasi IoT Sederhana", layout="centered")

st.title("🔌 Simulasi IoT Sederhana untuk Anak SMP")

st.markdown("""
## 💡 Contoh Kasus: Lampu Otomatis
Lampu akan menyala secara otomatis jika sensor mendeteksi bahwa ruangan gelap (nilai cahaya rendah).
""")

# Input simulasi dari pengguna
light_level = st.slider("Seberapa terang ruangan? (0 = Gelap, 100 = Terang)", 0, 100, 50)

# Simulasi logika IoT
if light_level < 30:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Light_bulb_icon.svg/1200px-Light_bulb_icon.svg.png", width=100)
    st.success("💡 Lampu otomatis MENYALA karena ruangan gelap.")
else:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Lightbulb_off_font_awesome.svg/1200px-Lightbulb_off_font_awesome.svg.png", width=100)
    st.info("💤 Lampu tetap MATI karena ruangan cukup terang.")

# Penjelasan singkat
st.markdown("""
---
### 🤔 Kenapa Bisa Begitu?
Ini adalah contoh dari **Internet of Things (IoT)**, di mana alat seperti sensor cahaya dan lampu dihubungkan untuk bekerja otomatis.

Dengan logika: `Jika cahaya < 30 maka nyalakan lampu`.

IoT membantu membuat kehidupan lebih mudah, hemat energi, dan pintar!
""")
