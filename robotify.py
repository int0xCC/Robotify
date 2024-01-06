from gtts import gTTS 

import os 

print("<<<<Text to Speech Coverter>>>>")

print("Type in the text for converting into speech:")

txt = input()

lang = 'en'
  
conv = gTTS(text=txt, lang=lang, slow=False) 
 
conv.save("cnvrt.mp3") 

os.system("mpg321 cnvrt.mp3") 
