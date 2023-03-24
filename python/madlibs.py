#import gtts
from gtts import gTTS
import os

name = "My name is "
cont = " and I'm currently learning "
cont1 = " at Try Kibo."
cont2 = " I'm joining the program from "
cont3 = "."
cont4 = " I plan to dedicate "
cont5 = " hours per day for the program."
cont6 = " At the end of this program, my goal is "
cont7 = " so that I can "
cont8 = " and make impact by "
cont9 = "."

#cont-continuation

firstname = input("Name: ")
course = input("course : ")
country = input("country : ")
hours = input("learning hrs/day: ")
goal = input("your goal : ")
intention = input("Your next plan is?: ")
impact = input("Impact to make: ")

result = name + firstname + cont + course + cont1 + cont2 + country + cont3 + cont4 + hours + cont5 + cont6 + goal + cont7 + intention + cont8 + impact + cont9

print("   ")
print("\n" + result)

language = 'en'
audio = gTTS(text=result, lang=language, slow=False)
audio.save("audio.mp3")
os.system("start audio.mp3")
'''

print("My name is " + firstname + " and I’m currently learning " + course + " at Try Kibo. I’m joining the program from " + country + "." + " I plan to dedicate " + hours + " hours per day for the program. At the end of this program, I want to " + goal + " so that I can " + intention + " and " + impact + ".")'''
