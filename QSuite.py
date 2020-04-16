#LIBRARIES
from __future__ import division
import re
import rtmidi
import mido
from mido import Message
from gpiozero import PWMLED
from signal import pause

#VARIABLES
led1 = PWMLED(17)
led2 = PWMLED(27)
led3 = PWMLED(22)

#ACTIONS
with mido.open_input('New Port', virtual=True) as inport:
	note = Message('note_on')
	notestr = str(note)
	#parse.string(notestr)
	for note in inport:
		print(note.velocity)
		#led1.value = float(note_on / 127.0)
	pause()
