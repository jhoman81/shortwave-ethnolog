"""
Shortwave Ethnographic Logging Tool
Author: Joshua Homan

TODO: Convert save_data() function to write to SQL database
TODO: Convert GUI to wxPython or other API
TODO: Implement timer function for each broadcast/call
TODO: Geo-code placenames
TODO: Implement JSON parsing of language file
TODO: Integrate kinship and social relationship information somehow -- autocomplete on speaker based on kinship database
TODO: Record line-in audio and link to DB entry for later analysis

"""

from tkinter import *
import tkinter.messagebox
from datetime import datetime
import json

class Place:
	def __init__(self, name, latitude, longitude):
		self.name = name
		self.latitude = latitude
		self.longitude = longitude

class Call:
	def __init__(self, place_one, place_two, participant_one, participant_two, topic, time, date):
		self.place_one = place_one
		self.place_two = place_two
		self.participant_one = participant_one
		self.participant_two = participant_two
		self.topic = topic
		self.time = time
		self.date = datetime(date)

def read_places(file):
    places = []
    with open(file, 'r') as place_file:
        for line in place_file:
            places.append(line.rstrip())
    return places

## Write data to textfile 

def save_data():
	try:
		fileD = open("swlog.txt", "a")
		fileD.write("Time and Date: ")
		fileD.write(str(datetime.now()))
		fileD.write("\n")
		fileD.write("Frequency: ")
		fileD.write("%s " % frequency.get())
		fileD.write("%s\n" % band.get())
		fileD.write("\nSpeaker One: %s\n" % speakerOne.get())
		fileD.write("Speaker One's Location: %s\n" % speakerOnePlace.get())
		fileD.write("\nSpeaker Two: %s\n" % speakerTwo.get())
		fileD.write("Speaker Two's Location: %s\n\n" % speakerTwoPlace.get())
		fileD.write("Language Used: %s\n\n" % language.get())
		fileD.write("Notes: %s\n\n" % notes.get("1.0", END))
		fileD.write("-=-" * 20)
		fileD.write("\n\n")
		band.set(None)
		speaker_one_place.set(None)
		speakerTwoPlace.set(None)
		frequency.delete(0, END)
		speakerOne.delete(0, END)
		speakerTwo.delete(0, END)
		language.set(None)
		notes.delete("1.0", END)
	except Exception as ex:
		tkinter.messagebox.showerror("Error!", "Can't write to the file\n %s" % ex)

## Construct GUI -- to convert to wxPython or other GUI
## If unable, try to make classes for positioning

app = Tk()
app.title('Shortwave Radio Log')

Label(app, text = "Frequency").pack()
frequency = Entry(app)
frequency.pack()

Label(app, text = "Band:").pack()
band = StringVar()
band.set("USB")
Radiobutton(app, variable = band, text = "USB", value = "USB").pack()
Radiobutton(app, variable = band, text = "LSB", value = "LSB").pack()

Label(app, text = "Speaker One").pack()
speakerOne = Entry(app)
speakerOne.pack()

Label(app, text = "Speaker One's Location").pack()
speaker_one_place = StringVar()
options_one = read_places("./places.txt")
speaker_one_place.set(None)
dropdown_one = OptionMenu(app, speaker_one_place, options_one)
dropdown_one['width'] = 10
dropdown_one.pack()

Label(app, text = "Speaker Two").pack()
speakerTwo = Entry(app)
speakerTwo.pack()

Label(app, text = "Speaker Two's Location").pack()
speakerTwoPlace = StringVar()
speakerTwoPlace.set(None)
optionsTwo = read_places("./places.txt")
dropdown_two = OptionMenu(app, speakerTwoPlace, optionsTwo)
dropdown_two['width'] = 10
dropdown_two.pack()

Label(app, text = "Language:").pack()
language = StringVar()
language.set("Spanish")
Radiobutton(app, variable = language, text = "Spanish", value = "Spanish").pack()
Radiobutton(app, variable = language, text = "Quechua", value = "Quechua").pack()
Radiobutton(app, variable = language, text = "Kandozi", value = "Kandozi").pack()
Radiobutton(app, variable = language, text = "Achuar", value = "Achuar").pack()

Label(app, text = "Notes").pack()
notes = Text(app)
notes.pack()

Button(app, text = "Save", command = save_data).pack()

## Main loop

if __name__ == "__main__":
	app.mainloop()