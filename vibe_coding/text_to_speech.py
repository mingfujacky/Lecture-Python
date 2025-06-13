# write a python program to turn a text file into an audio file
from gtts import gTTS
from pathlib import Path

def text_file_to_audio(input_txt_path, output_audio_path, lang='en'):
    # Read the text file
    with open(input_txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # Convert text to speech
    tts = gTTS(text=text, lang=lang)
    # Save the audio file
    tts.save(output_audio_path)
    print(f"Audio saved to {output_audio_path}")

if __name__ == "__main__":
    input_txt = Path.cwd() / "restricted" / "assets" / "text_to_speech" / "定風波.txt"
    output_mp3 = Path.cwd() / "restricted" / "assets" / "text_to_speech" / "定風波.mp3"
    text_file_to_audio(input_txt, output_mp3, lang='zh-cn')
    input_txt = Path.cwd() / "restricted" / "assets" / "text_to_speech" / "雙城記開頭.txt"
    output_mp3 = Path.cwd() / "restricted" / "assets" / "text_to_speech" / "雙城記開頭.mp3"
    text_file_to_audio(input_txt, output_mp3, lang='en')