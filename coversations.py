import re

def conv_txt():
    with open('movie_lines.txt', 'r') as ml, open('movie_conversations.txt', 'w') as mc:
        i = 1
        j = 2
        for line in ml:
            for k in range(0,14):
                if "m{}".format(k) in str(line):
                    l = '''u0 +++$+++ u1 +++$+++ m{} +++$+++ ['L{}', 'L{}']\n'''.format(k, j, i)
                    i += 2
                    j += 2
                    mc.write(l)

def conv_s2s():
    with open('movie_lines.txt', 'r') as ml, open('movie_conversations2.txt', 'w') as mc:
        for line in ml:
            pass

if __name__=='__main__':
    conv_txt()