import speech_recognition as sr
import skill
from playsound import playsound


skills = []
audio_text = ''

def is_in_wake_words(audio_text):
    """
    this function checks if the word
    said is one of the similar words to
    Dalela in wake_up_words.txt
    """

    file = open('wake_up_words.txt','r')

    similar_words = (file.read().split('\n'))  # making a list
    for word in similar_words:  # going over that list
        if word.lower() in audio_text.lower():
            not_wakeup_word = False
            print('it matches ' + word)
            return True
    return False


def look_for_trigger():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        not_wakeup_word = True

        while not_wakeup_word:  # keep listening as long as no trigger word recognized
            try:
                print("I am listening :")
                input_audio = r.listen(source)
                audio_text = r.recognize_google(input_audio)
                print("You said : {}".format(audio_text))
                if is_in_wake_words(audio_text):
                    not_wakeup_word = False
            except:
                print("not recognized by the API")

    if not (not_wakeup_word):
        playsound('beep.wav')


def start_listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("I am listening :")
            input_audio = r.listen(source)
            audio_text = r.recognize_google(input_audio)
            print("You said : {}".format(audio_text))
            if is_in_wake_words(audio_text):
                not_wakeup_word = False
            return audio_text
        except:
            print("not recognized by the API")


def start_replying(audio_text):
	found_reply = False
	for each_skill in skills:
		for choice in each_skill.input_choices:
			if choice == audio_text:
				each_skill.reply()
				found_reply = True
				print('skill found!')

	if not found_reply:
		print('no skill found')





"""
	Main code
"""

# look_for_trigger()
# audio_text = start_listening()
# start_replying(audio_text)

# todo: make a meathod that searches through skills to find the aprioperiate one (this is before nlp)
skill1 = skill.TrivialSkill()
skill1.readChoices('Age')
skill1.reply()





