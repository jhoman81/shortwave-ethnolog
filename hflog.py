"""
Shortwave Ethnographic Logging Tool
Author: Joshua Homan

TODO: Convert GUI to wxPython or other API
TODO: Implement timer function for each broadcast/call
TODO: Implement JSON parsing of language file
TODO: Record line-in audio and link to DB entry for later analysis

"""

from pathlib import Path
from tkinter import *
import tkinter.messagebox
from datetime import datetime
import json, csv

class Place:
	def __init__(self, name, latitude, longitude):
		self.name = name
		self.latitude = latitude
		self.longitude = longitude

	def __repr__(self):
		return self.name + " is located at the coordinates " + str(self.latitude) + ", " + str(self.longitude)

class Participant:
	def __init__(self, name):
		self.name = name

class Call:
	def __init__(self, place_one, place_two, participant_one, participant_two, topic, time, date, note):
		self.place_one = place_one
		self.place_two = place_two
		self.participant_one = participant_one
		self.participant_two = participant_two
		self.topic = topic
		self.time = time
		self.date = datetime(date)
		self.note = note

def read_places(file):
	filename = Path("./places.csv")
	places = []
	try:
		with open(filename, 'r', encoding='UTF8') as place_file:
			for line in place_file:
				places.append(line.rstrip())
	except EnvironmentError:
		print("File does not exist.")
	return places

def add_place(name, latitude, longitude):
	header = ["Name", "Latitude", "Longitude"]
	data = [name, latitude, longitude]
	filename = Path("./places.csv")
	if filename.is_file():
		with open(filename, 'a', encoding='UTF8') as place_file:
			writer = csv.writer(place_file)
			writer.writerow(data)
	else:
		with open(filename, 'w', encoding='UTF8') as place_file:
			writer = csv.writer(place_file)
			writer.writerow(header)
			writer.writerow(data)

def save_data():
	filename = Path("./swlog.md")
	if filename.is_file():
		with open(filename, 'a') as log_file:
			log_file.write("## New Entry")
			log_file.write("Time and Date: ")
			log_file.write(str(datetime.now()))
			log_file.write("\n")
			log_file.write("Frequency: ")
			log_file.write("%s " % frequency.get())
			log_file.write("%s\n" % band.get())
			log_file.write("\nSpeaker One: %s\n" % speaker_one.get())
			log_file.write("Speaker One's Location: %s\n" % speaker_onePlace.get())
			log_file.write("\nSpeaker Two: %s\n" % speaker_two.get())
			log_file.write("Speaker Two's Location: %s\n\n" % speaker_twoPlace.get())
			log_file.write("Language Used: %s\n\n" % language.get())
			log_file.write("Notes: %s\n\n" % notes.get("1.0", END))
			log_file.write("-=-" * 20)
			log_file.write("\n\n")
			band.set(None)
			speaker_one_place.set(None)
			speaker_one_place.set(None)
			frequency.delete(0, END)
			speaker_one.delete(0, END)
			speaker_two.delete(0, END)
			language.set(None)
			notes.delete("1.0", END)
	else:
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
speaker_one = Entry(app)
speaker_one.pack()

Label(app, text = "Speaker One's Location").pack()
speaker_one_place = StringVar()
options_one = read_places("./places.txt")
speaker_one_place.set(None)
dropdown_one = OptionMenu(app, speaker_one_place, options_one)
dropdown_one['width'] = 10
dropdown_one.pack()

Label(app, text = "Speaker Two").pack()
speaker_two = Entry(app)
speaker_two.pack()

Label(app, text = "Speaker Two's Location").pack()
speaker_twoPlace = StringVar()
speaker_twoPlace.set(None)
options_two = read_places("./places.txt")
dropdown_two = OptionMenu(app, speaker_twoPlace, options_two)
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