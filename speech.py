from gtts import *
import os
ado=gTTS(text="I am your Virtual Assistant please ask me  ", lang="en" ,slow=False)
sav="wel.mp3"
ado.save("wel.mp3")
os.system(f"start {sav}")