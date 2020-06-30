#importing packages

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import pyttsx3

#object creation

bot=ChatBot('ANN')
talk=pyttsx3.init()

#train the chatbot

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train('chatterbot.corpus.english')

#function makes talkbot to talk

def interact(reply):
    print('{}:{}'.format(bot.name,reply))
    talk.say(reply)
    talk.runAndWait()    

#making interaction with talkbot
    
while True:
    speech=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        print('{} listening...'.format(bot.name))
        audio=speech.listen(source)
    
    try:
        message=speech.recognize_google(audio)
        print('you: {}'.format(message))
        
        if(message=='bye see you later'):
            reply='I enjoyed talking to you,bye'
            interact(reply)
            break
        
        else:
            reply=bot.get_response(message)
            
    except:
        reply='Pardon,I am listening again'
    
    interact(reply)
        