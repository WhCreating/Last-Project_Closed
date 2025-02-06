import llama
import synthesis
import voicer
import asyncio
from config import conf
from os import path
import toml

def shell(model='.\\models\\small_model_ru', micros=2, mod='kal'):
    parent_dir = path.dirname(path.abspath(__file__))
    with open(path.join(parent_dir, 'settings', 'config.ini'), 'r') as f:
        confss = toml.load(f)

    global config
    config = confss



    c = voicer.recording(model, micros, mod)
    print(c)
    #return c

    if config['name_bot'] in c:
        l = c
        b = asyncio.run(llama.chat(c))
        synthesis.synthes(b)
        return f'Вы: {l}\nОтвет: {b}'
    else:
        l = c
        c = c.lower().split()
        c.append('')

        if c[0] in conf:
            v = conf[c[0]][c[1]]()
            return f'Вы: {l}\n'f'Ответ: {v}'
        else:
            synthesis.synthes('Такой команды нет!')
            return f'Вы: {l}\nОтвет: Такой команды нет!'









if __name__ == '__main__':
    shell(mod='gsrec')