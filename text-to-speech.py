from gtts import gTTS
import os

audios=gTTS(text="hello my dear freinds i fill the golu please go yaha ka time na kharab kare " ,lang ="en", slow=False)
sav="welcome.mp3"
audios.save("welcome.mp3")
os.system(f"start {sav}")
 