import pyttsx3
import random
import os


class TrivialSkill:

	def __init__(self):
		self.chosen_question = []
		self.chosen_answer = []


	def readChoices(self,skill_name):
		# print(os.getcwd())
		os.chdir(os.getcwd()+'/Trvial_Skills/Answers/') # todo: questions is answers <opposite!>

		file = open(skill_name)  # todo: should be changed (add .txt) when adding extentions
		questions = file.read()
		questions = questions.split('\n')
		self.chosen_question = random.choice(questions)

		os.chdir('../Questions/')

		file = open(skill_name)  # todo: should be changed (add .txt) when adding extentions
		answers = file.read()
		answers = answers.split('\n')
		self.chosen_answer = random.choice(answers)

		print(self.chosen_question + '\n' + self.chosen_answer)



	def reply(self):
		engine = pyttsx3.init()

		engine.say(self.chosen_answer)
		engine.runAndWait()

