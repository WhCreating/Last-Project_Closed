import os
import speech_recognition as sr
from pycparser.c_ast import Return


def main(audio, r):
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio_data=audio, language='ru-RU')
    except sr.UnknownValueError:
        return 'Вас не слышно, вы тут? Подключите микрофон.'
    except sr.RequestError as e:
        return "Не удалось подключиться к сервису google, чтобы распознать вашу речь, проверьте соединение с интернетом! {0}".format(e)

def name():
    return 'Google Speech Recognition'

def types():
    return 'voice_sp'