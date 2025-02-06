import json, pyaudio
from vosk import Model, KaldiRecognizer
#import synthesis
#from llama import chat
import asyncio
import os
import speech_recognition as sr
from mods import *
from logging import *
from os import path
import toml



def recording(models, micro: int, mod):
	all_imported_modules = import_all_modules()
	global parent_dir
	parent_dir = path.dirname(path.abspath(__file__))

	with open(path.join(parent_dir, 'settings', 'config.ini'), 'r') as f:
		confs = toml.load(f)

	global config
	config = confs


	if mod in all_imported_modules:

		if config['or_radio'] == 1 and all_imported_modules[mod].types() == 'voice_sp':
			r = sr.Recognizer()
			with sr.Microphone(device_index=micro - 1) as source:
				print("Say something!")
				audio = r.listen(source)

			return all_imported_modules[mod].main(audio, r)
		elif config['or_radio'] == 1 and all_imported_modules[mod].types() == 'custom':
			return all_imported_modules[mod].main(micro - 1, models)
		else:
			model = Model(models)
			rec = KaldiRecognizer(model, 16000)
			p = pyaudio.PyAudio()
			stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=10000, input_device_index=micro)
			stream.start_stream()

			def listen():
				while True:
					data = stream.read(4000, exception_on_overflow=False)
					if (rec.AcceptWaveform(data)) and (len(data) > 0):
						answer = json.loads(rec.Result())
						if answer['text']:
							yield answer['text']



			for text in listen():
				return text

	else :
		return error('Mods error, no mod available')

if __name__ == "__main__":
	print(recording('.\\models\\small_model_ru', 1, 'gsrec'))