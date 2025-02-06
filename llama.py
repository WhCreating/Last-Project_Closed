import asyncio
from ollama import AsyncClient
#import tensorflow as tf
from synthesis import synthes
from time import sleep
import threading

async def chat(promt):
    message = {'role': 'user', 'content': f'{promt}'}
    global a
    a = ''



    async for part in await AsyncClient().chat(model='llama3', messages=[message], stream=True):
        a += part['message']['content']


    return a


if __name__ == '__main__':
    print(asyncio.run(chat('Расскажи про верблюдов в 2 предложения')))

