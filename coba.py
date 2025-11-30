import streamlit as st
import pandas as pd

# --------------------------
# SIDEBAR
# --------------------------
st.sidebar.title("📌 Menu Navigasi")
menu = st.sidebar.radio(
    "Pilih fitur:",
    ("Beranda", "Kalkulator", "Upload Data", "Visualisasi Data")
)

# --------------------------
# BERANDA
# --------------------------
if menu == "Beranda":
    st.title("✨ Aplikasi Streamlit Serbaguna")
    st.write("""
    Aplikasi ini dibuat menggunakan **Streamlit** dan berisi beberapa fitur utama:
    
    **1. Kalkulator**  
    Melakukan operasi matematika sederhana.

    **2. Upload Data**  
    Mengunggah file Excel/CSV dan melihat isinya.

    **3. Visualisasi Data**  
    Membuat grafik otomatis dari data yang di-upload.

    Silakan pilih fitur di sebelah kiri untuk mulai.
    """)

# --------------------------
# KALKULATOR
# --------------------------
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Penjumlahan")

    angka1 = st.number_input("Masukkan angka pertama")
    angka2 = st.number_input("Masukkan angka kedua")

    if st.button("Hitung"):
        hasil = angka1 + angka2
        st.success(f"Hasil penjumlahan: **{hasil}**")

# --------------------------
# UPLOAD DATA
# --------------------------
elif menu == "Upload Data":
    st.title("📤 Upload File Excel / CSV")

    file = st.file_uploader("Pilih file", type=["xlsx", "csv"])

    if file is not None:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.subheader("📄 Tampilan Data")
        st.dataframe(df)

        st.success("Data berhasil di-upload!")

# --------------------------
# VISUALISASI DATA
# --------------------------
elif menu == "Visualisasi Data":
    st.title("📊 Grafik Otomatis dari Data")

    file = st.file_uploader("Upload file (Excel/CSV)", type=["xlsx", "csv"], key="visual")

    if file is not None:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.subheader("📄 Data")
        st.dataframe(df)

        # Pilih kolom untuk sumbu X dan Y
        st.subheader("⚙ Pengaturan Grafik")
        kolom = df.columns.tolist()

        x = st.selectbox("Pilih kolom X:", kolom)
        y = st.selectbox("Pilih kolom Y:", kolom)

        st.subheader("📈 Grafik Garis")
        st.line_chart(df.set_index(x)[y])

        st.subheader("📊 Grafik Bar")
        st.bar_chart(df.set_index(x)[y])