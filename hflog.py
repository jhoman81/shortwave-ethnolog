"""
Shortwave Ethnographic Logging Tool
Author: Joshua Homan

TO-DO: 

1. Convert save_data() function to write to SQL database
2. Convert GUI to wxPython or other API
3. Pickle placenames file and write de-pickle function
4. Implement timer function for each broadcast/call
5. Geo-code placenames and connect to ArcGIS database to run analysis for connections between communities -- placenames coordinates should be tab-delimited
6. Integrate kinship and social relationship information somehow -- autocomplete on speaker based on kinship 
   database (with connectiosn already set)
7. Record line-in and link to DB entry for later analysis

"""

from tkinter import *
import tkinter.messagebox
from datetime import datetime

## Read placenames from file -- how to geocode this for future analysis?

def read_places(file):
    places = []
    place_f = open(file)
    for line in place_f:
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
		speakerOnePlace.set(None)
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
app.title('Shortwave Amazonia - Radio Log')

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
speakerOnePlace = StringVar()
speakerOnePlace.set(None)
optionsOne = read_places("places.txt")
OptionMenu(app, speakerOnePlace, *optionsOne).pack()

Label(app, text = "Speaker Two").pack()
speakerTwo = Entry(app)
speakerTwo.pack()

Label(app, text = "Speaker Two's Location").pack()
speakerTwoPlace = StringVar()
speakerTwoPlace.set(None)
optionsTwo = read_places("places.txt")
OptionMenu(app, speakerTwoPlace, *optionsTwo).pack()

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