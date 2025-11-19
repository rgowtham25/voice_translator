import gradio as gr
import assemblyai as aai
from translate import Translator
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import uuid
from pathlib import Path

def voice_to_voice(audio_file):
    
    #transcribe audio
    transcription_response = audio_transcription(audio_file)

    if transcription_response.status == aai.TranscriptStatus.error:
        raise gr.Error(transcription_response.error)
    else:
        text = transcription_response.text

    ta_translation, te_translation, ml_translation = text_translation(text)

    ta_audi_path = text_to_speech(ta_translation)
    te_audi_path = text_to_speech(te_translation)
    ml_audi_path = text_to_speech(ml_translation)

    ta_path = Path(ta_audi_path)
    te_path = Path(te_audi_path)
    ml_path = Path(ml_audi_path)

    return ta_path, te_path, ml_path


def audio_transcription(audio_file):

    aai.settings.api_key = ".........................."

    try:
        transcriber = aai.Transcriber()
        config = aai.TranscriptionConfig(language_code="en")
        transcription = transcriber.transcribe(audio_file, config=config)
        return transcription
    except Exception as e:
        print(f"Transcription error: {str(e)}")
        raise gr.Error(f"Failed to transcribe audio: {str(e)}")

def text_translation(text):
    
    translator_ta = Translator(from_lang="en", to_lang="ta")
    ta_text = translator_ta.translate(text)

    translator_te = Translator(from_lang="en", to_lang="te")
    te_text = translator_te.translate(text)

    translator_ml = Translator(from_lang="en", to_lang="ml")
    ml_text = translator_ml.translate(text)

    return ta_text, te_text, ml_text

def text_to_speech(text):

    client = ElevenLabs(
        api_key= "sk.....",
    )

    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="......................", #clone your voice on elevenlabs dashboard and copy the id
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path

audio_input = gr.Audio(
    sources=["microphone"],
    type="filepath",
    format="wav"
)

demo = gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=[gr.Audio(label="Tamil"), gr.Audio(label="Telugu"), gr.Audio(label="Malayalam")]
)

if __name__ == "__main__":
    demo.launch()
