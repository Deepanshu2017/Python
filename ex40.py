class song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

my_first_song = song(['Love the way you lie','Go hard or go home','Tuna mara jana, kabhi nhi jana'])
my_last_song = song(['gyatri mantra','I love my country'])

my_first_song.sing_me_a_song()
my_last_song.sing_me_a_song()
