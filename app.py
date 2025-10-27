import streamlit as st
from gtts import gTTS
import os
from io import BytesIO
import base64

# Configuración de la página
st.set_page_config(
    page_title="Texto a Voz - Español Latino",
    page_icon="🔊",
    layout="centered"
)

# Título de la aplicación
st.title("🔊 Conversor de Texto a Voz")
st.subheader("Español Latino")

# Área de texto para entrada
texto_input = st.text_area(
    "Escribe el texto que deseas convertir a voz:",
    height=150,
    placeholder="Escribe aquí tu texto..."
)

# Botón para generar el audio
if st.button("🎤 Generar Voz", type="primary"):
    if texto_input.strip():
        with st.spinner("Generando audio..."):
            try:
                # Crear objeto de texto a voz con español latino
                # 'es' para español, con acento mexicano por defecto
                # Puedes usar 'es-us' para español de Estados Unidos
                tts = gTTS(text=texto_input, lang='es', slow=False, tld='com.mx')
                
                # Guardar en un objeto BytesIO en lugar de archivo
                audio_bytes = BytesIO()
                tts.write_to_fp(audio_bytes)
                audio_bytes.seek(0)
                
                # Guardar en session_state para mantener el audio
                st.session_state['audio_data'] = audio_bytes.getvalue()
                st.success("✅ Audio generado exitosamente!")
                
            except Exception as e:
                st.error(f"Error al generar el audio: {str(e)}")
    else:
        st.warning("⚠️ Por favor, escribe algún texto primero.")

# Mostrar reproductor y opción de descarga si existe audio generado
if 'audio_data' in st.session_state:
    st.markdown("---")
    st.subheader("🎧 Reproducir Audio")
    
    # Reproductor de audio con controles (play, pause)
    st.audio(st.session_state['audio_data'], format='audio/mp3')
    
    # Botón de descarga
    st.download_button(
        label="⬇️ Descargar Audio MP3",
        data=st.session_state['audio_data'],
        file_name="audio_generado.mp3",
        mime="audio/mp3"
    )

# Información adicional
with st.expander("ℹ️ Información"):
    st.markdown("""
    **Características:**
    - Conversión de texto a voz en español latino
    - Reproductor con controles de pausa y reproducción
    - Descarga del audio en formato MP3
    
    **Instrucciones:**
    1. Escribe o pega tu texto en el área de texto
    2. Haz clic en "Generar Voz"
    3. Usa el reproductor para escuchar el audio
    4. Descarga el archivo MP3 si lo deseas
    
    **Nota:** Esta aplicación utiliza Google Text-to-Speech (gTTS) con acento mexicano.
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Desarrollado con Streamlit y gTTS</div>",
    unsafe_allow_html=True
)