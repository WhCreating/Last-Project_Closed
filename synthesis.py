import pyttsx3

def synthes(text):
	engine = pyttsx3.init()

	engine.say(text)
	engine.runAndWait()

if __name__=="__main__":
	synthes('Тест синтеза hello')