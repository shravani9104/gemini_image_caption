# AI-Powered Image Caption Generator using Gemini API

This project uses Google Gemini API to generate captions for images uploaded by users. The captions are then read aloud using gTTS (Google Text-to-Speech). The project is built using Streamlit, a framework to create interactive web applications, and integrates AI to generate captions for images.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The AI-Powered Image Caption Generator is an interactive web app that lets users upload an image, generate a caption using the Google Gemini API, and listen to the caption through Google Text-to-Speech (gTTS).

### Key Features:
- Image Upload: Upload `.jpg`, `.jpeg`, `.png` images.
- Caption Generation: The Google Gemini API generates a detailed caption for the uploaded image.
- Download Caption: Download the generated caption as a `.txt` file.
- Text-to-Speech: Listen to the caption through gTTS (Google Text-to-Speech).

## Features

- Image Upload: Users can upload images in various formats (`.jpg`, `.jpeg`, `.png`).
- Caption Generation: AI uses the Google Gemini API to generate captions for the uploaded image.
- Download Caption: Once the caption is generated, users can download it as a `.txt` file.
- Text-to-Speech: After generating the caption, the app will automatically play the caption aloud.

## Requirements

This project has the following dependencies:

- Streamlit: For building the interactive web interface.
- Google Generative AI: To interact with the Google Gemini API and generate image captions.
- gTTS: For converting the caption into speech.
- Pillow: For working with image files.
- python-dotenv: For managing environment variables securely.

### Install the required dependencies

1. Clone the repository or download the project files.
2. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
