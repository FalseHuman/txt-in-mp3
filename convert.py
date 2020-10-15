from gtts import gTTS 

audio = 'audio.mp3'
language = 'ru'

sp = gTTS(text=input(), lang=language, slow=False)

sp.save(audio)