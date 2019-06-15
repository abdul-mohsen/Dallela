import speech_recognition as sr
from playsound import playsound



def is_in_wake_words(audio_text):
    '''
    this function checks if the word
    said is one of the similar words to
    Dalela
    '''

    file = open('wake_up_words','r')

    similar_words = (file.read().split('\n'))
    for word in similar_words:
        if word.lower() in audio_text.lower():
            not_wakeup_word = False
            print('it matches ' + word)
            return True
    return False


r = sr.Recognizer()
with sr.Microphone() as source:
    not_wakeup_word = True

    while not_wakeup_word:
        try:
            print("Speak Anything :")
            input_audio = r.listen(source)
            audio_text = r.recognize_google(input_audio)
            print("You said : {}".format(audio_text))
            if is_in_wake_words(audio_text):
                not_wakeup_word = False
        except:
            print("not recognized")

if not (not_wakeup_word):
    playsound('beep.wav')




