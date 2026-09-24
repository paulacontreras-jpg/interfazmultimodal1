import streamlit as st
import os
import time
import glob
from gtts import gTTS
from PIL import Image
import base64

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="Texto a Audio - El Renacuajo Paseador",
    page_icon="🐸",
    layout="wide"
)

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

st.markdown("""
<style>

    /* Fondo */
    .stApp {
        background: #F4FAF2;
    }

    /* Barra lateral */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #245C3A 0%, #3E8054 100%);
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: white;
    }

    /* Encabezado */
    .titulo {
        background: linear-gradient(135deg, #245C3A, #5C9E68);
        color: white;
        padding: 35px;
        border-radius: 25px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 8px 20px rgba(36, 92, 58, 0.20);
    }

    .titulo h1 {
        font-size: 40px;
        margin-bottom: 8px;
    }

    .titulo p {
        font-size: 17px;
        margin: 0;
    }

    /* Tarjeta de la fábula */
    .fabula {
        background: white;
        padding: 25px;
        border-radius: 20px;
        border-left: 8px solid #6BAE75;
        box-shadow: 0px 5px 18px rgba(50, 100, 60, 0.12);
        margin-bottom: 25px;
    }

    .fabula h3 {
        color: #245C3A;
    }

    .fabula p {
        color: #444444;
        line-height: 1.7;
        font-size: 16px;
    }

    /* Caja de texto */
    .editor {
        background: #E4F2E4;
        padding: 20px;
        border-radius: 18px;
        margin-top: 20px;
    }

    /* Botón */
    .stButton > button {
        background: #3E8054;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 25px;
        font-weight: bold;
        font-size: 16px;
    }

    .stButton > button:hover {
        background: #F0C95C;
        color: #245C3A;
    }

    /* Separadores */
    .decoracion {
        color: #6BAE75;
        font-size: 25px;
        text-align: center;
        margin: 15px;
    }

    /* Caja del audio */
    .audio-box {
        background: #EAF6E8;
        border: 2px solid #9ACB9F;
        padding: 20px;
        border-radius: 18px;
        margin-top: 20px;
    }

    .audio-box h3 {
        color: #245C3A;
    }

    /* Pie de página */
    .footer {
        text-align: center;
        color: #4D8058;
        padding: 25px;
        margin-top: 35px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# BARRA LATERAL
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 🐸 Texto a Audio")

    st.markdown("---")

    st.markdown("### 🎙️ ¿Cómo funciona?")

    st.write(
        "Escribe o selecciona un texto y conviértelo en "
        "audio utilizando Inteligencia Artificial."
    )

    st.markdown("---")

    st.markdown("### 🌿 Opciones")

    st.write("📝 Escribe tu texto")
    st.write("🌎 Selecciona el idioma")
    st.write("🎧 Genera el audio")
    st.write("⬇️ Descarga el resultado")


# --------------------------------------------------
# ENCABEZADO
# --------------------------------------------------

st.markdown("""
<div class="titulo">

<h1>🐸 Conversión de Texto a Audio</h1>

<p>El Renacuajo Paseador · Rafael Pombo</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# IMAGEN
# --------------------------------------------------

col_img1, col_img2, col_img3 = st.columns([1, 2, 1])

with col_img2:
    image = Image.open("rana.jpg.jfif")
    st.image(image, width=350)


st.markdown(
    "<div class='decoracion'>🌿 🐸 🌿</div>",
    unsafe_allow_html=True
)


# --------------------------------------------------
# FÁBULA
# --------------------------------------------------

st.markdown("""
<div class="fabula">

<h3>📖 Una fábula de Rafael Pombo</h3>

<p>
El hijo de Rana, Rinrín renacuajo,<br>
salió esta mañana muy tieso y muy majo<br>
con pantalón corto, corbata a la moda,<br>
sombrero encintado y chupa de boda.<br><br>

—¡Muchacho, no salgas! —le grita mamá,<br>
pero él hace un gesto y orondo se va.
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ÁREA DE TEXTO
# --------------------------------------------------

st.markdown("""
<div class="editor">

<h3>📝 Escribe el texto que quieres escuchar</h3>

<p>
Puedes copiar el fragmento anterior o escribir tu propio texto.
</p>

</div>
""", unsafe_allow_html=True)

text = st.text_area(
    "Ingrese el texto a escuchar:",
    height=150,
    placeholder="Escribe aquí el texto que quieres convertir en audio..."
)


# --------------------------------------------------
# IDIOMA
# --------------------------------------------------

option_lang = st.selectbox(
    "🌎 Selecciona el idioma",
    ("Español", "English")
)

if option_lang == "Español":
    lg = "es"
else:
    lg = "en"


# --------------------------------------------------
# FUNCIÓN TEXTO A AUDIO
# --------------------------------------------------

def text_to_speech(text, tld, lg):

    tts = gTTS(text, lang=lg)

    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"

    tts.save(f"temp/{my_file_name}.mp3")

    return my_file_name, text


# --------------------------------------------------
# CARPETA TEMPORAL
# --------------------------------------------------

try:
    os.mkdir("temp")
except:
    pass


# --------------------------------------------------
# BOTÓN DE CONVERSIÓN
# --------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🐸 Convertir a Audio"):

    if text.strip() == "":
        st.warning("⚠️ Primero escribe un texto para convertirlo en audio.")

    else:

        result, output_text = text_to_speech(text, "com", lg)

        audio_file = open(
            f"temp/{result}.mp3",
            "rb"
        )

        audio_bytes = audio_file.read()

        st.markdown("""
        <div class="audio-box">

        <h3>🎧 Tu audio está listo</h3>

        <p>
        Escucha el resultado de la conversión:
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.audio(
            audio_bytes,
            format="audio/mp3",
            start_time=0
        )

        # --------------------------------------------------
        # DESCARGA
        # --------------------------------------------------

        with open(f"temp/{result}.mp3", "rb") as f:

            data = f.read()

        def get_binary_file_downloader_html(
            bin_file,
            file_label="File"
        ):

            bin_str = base64.b64encode(data).decode()

            href = (
                f'<a href="data:application/octet-stream;base64,{bin_str}" '
                f'download="{os.path.basename(bin_file)}">'
                f'⬇️ Descargar {file_label}'
                f'</a>'
            )

            return href

        st.markdown(
            get_binary_file_downloader_html(
                "audio.mp3",
                file_label="Audio"
            ),
            unsafe_allow_html=True
        )


# --------------------------------------------------
# LIMPIEZA DE ARCHIVOS
# --------------------------------------------------

def remove_files(n):

    mp3_files = glob.glob("temp/*mp3")

    if len(mp3_files) != 0:

        now = time.time()
        n_days = n * 86400

        for f in mp3_files:

            if os.stat(f).st_mtime < now - n_days:

                os.remove(f)

                print("Deleted ", f)


remove_files(7)


# --------------------------------------------------
# PIE DE PÁGINA
# --------------------------------------------------

st.markdown("""
<div class="footer">

<div class="decoracion">🌱 🐸 🌱</div>

<b>Explora la conversión de texto a voz con Inteligencia Artificial</b>

<br>

Convierte tus palabras en sonido.

</div>
""", unsafe_allow_html=True)
