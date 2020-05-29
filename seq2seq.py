import re


with open('5.txt', 'r') as ml, open('6.txt', 'w') as s2s:
    pattern = r'  +++$+++'
    for line in ml:
        l = line.replace(pattern,'')
        s2s.write(l)