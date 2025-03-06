import os
from synthesis import synthes
import webbrowser


def hello():
    synthes("Чем могу помочь?")
    return "Чем могу помочь?"

def opens():
    synthes("Открываю")
    os.system("start https:// --start-fullscreen")
    return 'Открываю'

def open_browser(a):
    synthes("Открываю")
    if a == 'edge':
        os.system("start msedge.exe --start-fullscreen")
    elif a == 'chrome':
        os.system("start chrome.exe --start-fullscreen")
    elif a == 'firefox':
        os.system("start firefox.exe --start-fullscreen")

    return 'Открываю'

def opens_youtube():
    synthes("Открываю")
    webbrowser.open('https://www.youtube.com/', new=2)
    return 'Открываю'

def open_folder():
    synthes('Открываю')
    os.system("start explorer.exe")
    return 'Открываю'

def open_project():
    synthes("Открываю")
    webbrowser.open('https://www.last.ai.tilda.ws/', new=2)
    return 'Открываю'

if __name__ == '__main__':
    opens_youtube()