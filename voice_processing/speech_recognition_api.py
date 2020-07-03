import speech_recognition as sr
import os

# # obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

# use the audio file as the audio source
r = sr.Recognizer()

def speech_to_text(audio_file):
    try:
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)  # read the entire audio file
    except Exception:
        print('No such file or directory: ' + audio_file)
        # os.remove(audio_file)

    # recognize speech using Google Speech Recognition
    try:
        text_recognized = r.recognize_google(audio, language="vi-VN")
        print("Google Speech Recognition thinks you said in Vietnamese: " + text_recognized)
        return text_recognized
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
