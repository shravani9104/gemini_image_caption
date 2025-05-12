import google.generativeai as genai
from PIL import Image
from gtts import gTTS
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_caption(image_file):
    # Using the Gemini 1.5 Flash model
    model = genai.GenerativeModel('gemini-1.5-flash')
    image = Image.open(image_file)

    # Generate caption
    response = model.generate_content([
        "Describe this image in a single detailed sentence:",
        image
    ])
    return response.text.strip()

def save_caption(caption, filename="caption.txt"):
    # Save the caption to a text file
    with open(filename, "w") as f:
        f.write(caption)

def speak_caption(caption, filename="caption.mp3"):
    # Convert caption to speech and save it to an mp3 file
    tts = gTTS(text=caption, lang='en', slow=False)
    tts.save(filename)
    return filename  # Return file path for Streamlit
