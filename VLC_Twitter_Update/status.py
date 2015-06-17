__author__ = 'deepanshu'

import os
command = "lsof -c vlc 2>/dev/null | grep REG | grep -v -e '\.[ms]o' -e 'SYSV' -e 'font'"
audio_list = ['mp3', '3gp', 'au', 'wav', 'aiff', 'dvf', 'm4p', 'mmf', 'wma', 'msv']
video_list = ['mp4', 'flv', 'mov', 'mkv', 'avi']


def status():
    command_output = os.popen(command,'r')
    lines = command_output.readlines()
    if lines:
        # print '*' * 20    #Debug
        last = lines[-1]
        full_path = ' '.join(last.split()[8:]).strip()
        # print full_path.split('.')   #Debug
        for elem in full_path.split('.'):
            if elem in video_list:
                return {'vlc': True, 'type': 'video', 'path': full_path}
            elif elem in audio_list:
                return {'vlc': True, 'type': 'audio', 'path': full_path}
        else:
            return {'vlc': 'true', 'type': None, 'path': None}
    else:
        return {'vlc': False}
