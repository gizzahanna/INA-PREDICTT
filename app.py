import streamlit as st
import os

st.set_page_config(
    page_title="INA-PREDICT | Early Warning System",
    page_icon="🌋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS untuk styling Streamlit
st.markdown("""
<style>
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppHeader {display: none;}
    
    /* Main container */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    
    /* Make iframe full width */
    iframe {
        width: 100%;
        height: calc(100vh - 0px);
        border: none;
        margin: 0;
        padding: 0;
    }
    
    /* Hide Streamlit branding */
    .stAppDeployButton {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Menu navigasi untuk multiple pages
page = st.sidebar.radio(
    "Pilih Menu",
    ["Dashboard", "Prediksi Bencana", "Panduan Aksi", "Kontak Darurat", "Donasi", "Hubungi Kami"],
    index=0
)

# Mapping halaman ke file HTML
html_files = {
    "Dashboard": "index.html",
    "Prediksi Bencana": "prediksi.html",
    "Panduan Aksi": "panduan.html",
    "Kontak Darurat": "kontak.html",
    "Donasi": "donasi.html",
    "Hubungi Kami": "hubungikami.html"
}

# Baca file HTML
def load_html(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        # Fallback jika file tidak ditemukan
        return f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="UTF-8"><title>Error</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>❌ File tidak ditemukan</h1>
            <p>File {filename} tidak ditemukan. Pastikan semua file HTML berada di direktori yang sama dengan app.py</p>
        </body>
        </html>
        """

# Tampilkan halaman yang dipilih
st.components.v1.html(
    load_html(html_files[page]),
    height=800,
    scrolling=True
)

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 INA-PREDICT")
st.sidebar.caption("Early Warning System Indonesia")
st.sidebar.caption("Sumber: BNPB - BMKG - BPBD")