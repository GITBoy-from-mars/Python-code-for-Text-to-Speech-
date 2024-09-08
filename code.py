import os
# generate text and save it in random name
from gtts import gTTS

import uuid
from IPython.display import Audio

name = input(("enter text to want to speach: "))

names = gTTS(text=name, lang='en')

# i=1
for i in range (1,2):
  # def save (name):
  new = names.save(str(i) +".mp3")
  # i=i+1 
else: 
  new = str(uuid.uuid4())
  names.save(new + ".mp3")
  # ("outputs1.mp3")
os.remove(f"{new}.mp3")

print(f"The recent file name is {i}.mp3")
Audio(f"{i}.mp3")
