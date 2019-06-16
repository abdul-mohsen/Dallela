import pyttsx3
import random


class Skill:

	def __init__(self, one_input, one_output):
		self.input_choices = []
		self.output_choices = []

		for choice in one_input:
			self.input_choices.append(choice)

		for choice in one_output:
			self.output_choices.append(choice)

	def reply(self):
		engine = pyttsx3.init()

		random_reply = random.choice(self.output_choices)
		engine.say(random_reply)
		engine.runAndWait()

