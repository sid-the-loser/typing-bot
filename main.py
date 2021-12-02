import keyboard
from time import sleep
from os import system, name
from json import dump, load

default_settings = {
    "start_delay" : 10,
    "delay" : 45,
    "text" : ["hello world", "I'm dumb"]
}

file_ = open("Instructions.txt", "w")
file_.write("""If you don't have the settings.json file visible, then, run the file to generate the json file, don't press enter, just close it.

If you damaged the json file, then, delete the file and follow the first step to generate the file.

Then open the settings file, where you will be greeted with some things like:

start_delay, delay, text

start_delay:
	
	this gives you time to switch windows to discord

delay:

	this is the time taken between each session of messages

text:

	this is just a list of things that you wanna type in one burst

	WARNING: YOU COULD GET BANNED FOR SPAMMING IF YOU MAKE THE BURST BIGGER

thats all, bi""")
file_.close()

try:
    file_ = open("settings.json", "r")
except:
    file_ = open("settings.json", "w"); dump(default_settings, file_); file_.close()
    file_ = open("settings.json", "r")

settings = load(file_)
file_.close()
n = 0

input("Press enter to start the code...")
print("The code will start pressing buttons in", settings["start_delay"], "seconds!\n")
print("Press Ctrl-C on this window to close the window!\n")
sleep(settings["start_delay"])

while True:
    n += 1
    for text in settings["text"]:
        keyboard.write(text)
        keyboard.press("enter")
        keyboard.release("enter")
    print("Looped", n, "times")
    sleep(settings["delay"])
