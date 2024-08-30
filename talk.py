from gtts import gTTS
import os
audio=gTTS(text="Python decorators are really cool, but they can be a little hard to understand at first. A decorator in Python is a function that accepts another function as an argument. The decorator will usually modify or enhance the function it accepted and return the modified function. This means that when you call a decorated function, you will get a function that may be a little different that may have additional features compared with the base definition. But let’s back up a bit. We should probably review the basic building block of a decorator, namely, the function.", lang="en", slow=False)
mp3=("k.mp3")
audio.save(mp3)
os.system(f"start {mp3}")