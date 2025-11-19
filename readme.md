# AI Voice Translator

Record yourself speaking in English and get instant voice translations in **Tamil**, **Telugu**, and **Malayalam**. The translations are read back in your own cloned voice!

## Features

- 🎤 Real-time speech-to-text transcription
- 🌍 Translate English to Tamil, Telugu, and Malayalam
- 🔊 Text-to-speech with voice cloning
- 🎯 Simple web interface powered by Gradio

## Technologies Used

- **Gradio** - Web interface framework
- **AssemblyAI** - Speech-to-text transcription
- **Python Translate** - Text translation module
- **ElevenLabs** - Text-to-speech with voice cloning

## Getting Started

### Prerequisites

- Python 3.8+
- Required API keys:
  - [AssemblyAI API Key](https://www.assemblyai.com/)
  - [ElevenLabs API Key](https://elevenlabs.io/)

### Installation

1. Install dependencies:
```bash
pip install gradio assemblyai elevenlabs translate
```

2. Update API keys in `voice_translator.py`:
   - Replace the AssemblyAI API key on line 34
   - Replace the ElevenLabs API key on line 56

3. Run the application:
```bash
python voice_translator.py
```

The app will launch at `http://127.0.0.1:7860`

## Voice Cloning Setup

To use your own voice:
1. Clone your voice on the [ElevenLabs Dashboard](https://elevenlabs.io/app/voice-lab/add)
2. Copy your voice ID from the dashboard
3. Replace the `voice_id` in `voice_translator.py` (line 59)

Note: ElevenLabs offers free voice cloning with limited API usage.

## File Structure

- `voice_translator.py` - Main application (currently active)
- `readme.md` - This file