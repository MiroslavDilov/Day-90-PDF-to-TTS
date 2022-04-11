from gtts import gTTS


def make_tts_file(text, path):
    tts = gTTS(text)

    tts.save(f"{path}/file.mp3")