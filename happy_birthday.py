from pylab import *

def sing_hb(name):
    song = ''
    hb = 'Happy Birthday'
    
    for i in range(4):
        if i != 2:
            song += '%s to you,\n' % hb
        else:
            song += '%s dear %s,\n' % (hb, name)
    
    return song


if __name__ == "__main__":
    
    print sing_hb('Jacob')