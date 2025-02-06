from config_main import *
from synthesis import synthes


def build_dict(*pairs):
    d = {}
    for keys, value in pairs:
        d.update(dict.fromkeys(keys, value))
    return d

conf = build_dict(
    ((""), lambda: print("Укажите голосовую команду!")),
    (("привет", ""), {"":lambda : synthes("Чем могу помочь?")}),
    (("открой", "открывай"), {'браузер':lambda : opens(),
                'youtube':lambda : opens_youtube(),
                'ютуб':lambda : opens_youtube(),
                'папку': lambda : open_folder(),
                'проект': lambda : open_project(),
                'edge': lambda : open_browser('edge'),
                'chrome': lambda : open_browser('chrome'),
                'firefox': lambda : open_browser('firefox')
                              })



)

print(conf)




