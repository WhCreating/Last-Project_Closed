import pyaudio
import speech_recognition

def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    
    numdevices = info.get('deviceCount')
    mic_list = []

    for i in range(0, numdevices):
        if p.get_device_info_by_index(i).get('maxInputChannels') > 0:
            mic_list.append(p.get_device_info_by_index(i).get('name'))
    
    '''for i, mic in enumerate(mic_list):
        print(f"{i}:{mic}")'''

    return mic_list





if __name__ == '__main__':
    print(list_microphones())