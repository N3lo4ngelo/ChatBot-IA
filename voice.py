from gtts import gTTS


def text_to_voice(text, audio):
    tts = gTTS(text, lang="pt-br")

    tts.save(audio)

    print(f"Áudio salvo como {audio}")