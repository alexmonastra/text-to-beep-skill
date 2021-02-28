from mycroft import MycroftSkill
from mycroft.util import play_audio_file
import random
import time

class TextToBeep(MycroftSkill):
    def initialize(self):
        self.add_event("recognizer_loop:record_end", self.end_recording_sound)
        self.add_event("speak", self.play_sound)

    print('Loading Communication Relay...')
    

    def end_recording_sound(self, message):
        
        #Plays an audio cue so you know when mycroft is done listening
        
        play_audio_file("/home/alex/mycroft-core/mycroft/res/snd/BD1_end_listening.wav")
    

    def play_sound(self, message):
        
        #Plays a short or long (or both) audio clip depending on the length of the "Speak" message
        
        speak_text = str(message.data.get('utterance'))
        speak_len = len(speak_text)
        
        print("There are {} characters in this sentence.".format(speak_len))
        
        def play_short_sound():
            number = random.randint(1,46)
            audio = "/home/alex/mycroft-core/mycroft/res/snd/BD1/Sounds/BD1_Sounds_{}.wav".format(number)
            play_audio_file(audio)

        def play_talking_sound():
            number = random.randint(1,19)
            audio = "/home/alex/mycroft-core/mycroft/res/snd/BD1/Talking/BD1_Talking_{}.wav".format(number)
            play_audio_file(audio)       
            
        if speak_len <= 30:
            play_short_sound()
            
        elif speak_len > 30 and speak_len <= 60:
            play_talking_sound()
            
        elif speak_len > 60:
            play_short_sound()
            time.sleep(2)
            play_talking_sound()
        
def create_skill():
    return TextToBeep()

