import streamlit as st
from utils import generate_caption, save_caption, speak_caption
from PIL import Image

# Set page config
st.set_page_config(page_title="🧠 AI Image Caption Generator", layout="centered")

st.title("📸 AI-Powered Image Caption Generator using Gemini API")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate caption when button is pressed
    if st.button("✨ Generate Caption"):
        with st.spinner("Thinking..."):
            caption = generate_caption(uploaded_file)
            st.success("✅ Caption Generated!")
            st.write("📝 **Caption:**", caption)

            # Save caption to file
            save_caption(caption)

            # Allow downloading the caption text
            st.download_button("📄 Download Caption", data=caption, file_name="caption.txt", mime="text/plain")

            # Automatically speak the caption after it's generated
            audio_path = speak_caption(caption)
            with open(audio_path, "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3", start_time=0)
