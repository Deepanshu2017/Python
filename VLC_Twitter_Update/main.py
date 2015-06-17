__author__ = 'deepanshu'

from status import status
from compose_tweet import compose_tweet
import ntpath
from apscheduler.schedulers.blocking import BlockingScheduler
import logging        # Look at this (below) I am also not sure about it :(
logging.basicConfig()
# http://stackoverflow.com/questions/17528363/no-handlers-could-be-found-for-logger-apscheduler-scheduler

vlc_state = None


def parse_path(path):
    abs_path, name = ntpath.split(path)
    return name or ntpath.basename(abs_path)


def state():
    data = status()
    # print data    #Debug
    if data['vlc']:
        if data['type'] == 'video':
            return [True, 'Watching', parse_path(data['path'])]
        elif data['type'] == 'audio':
            return [True, 'Listening to', parse_path(data['path'])]
        else:
            return [True, 'your are not playing anything on VLC', '']
    else:
        return [False, 'VLC is not running', '']

job = BlockingScheduler()


@job.scheduled_job('interval', seconds=3)
def jobs():
    global vlc_state
    vlc_current_state = state()
    if vlc_current_state != vlc_state:
        vlc_state = vlc_current_state
        current_status = ' '.join(vlc_state[1:])
        if vlc_state[0] and vlc_state[2]:
            # print '*' * 20    #Debug
            print current_status
            compose_tweet('Deepanshu Thakur is ' + current_status + ' via python script')
        else:
            print current_status
job.start()

if __name__ == '__main__':
    vlc_state = state()
    print ' '.join(vlc_state[1:])
    job.start()
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print "Quitting"
            exit(0)
