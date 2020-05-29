import re, os
import multiprocessing as mp

def clear_time():
    pattern = r'\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d|\d{1,}|-'
    try:
        f = open("srt/13.srt")
        dirty = open("dirty.txt", 'w')
        for line in f:
            match = re.search(pattern, line)
            if match:
                l = re.sub(pattern, r'', line)
                dirty.write(l)

            else:
                if not line.isspace():
                    l2 = line.replace('\n', '')
                    dirty.write(l2)
                # dirty.write(line)

    except Exception as e:
        print(e)


def del_lines():
    with open('dirty.txt', 'r') as inf, open('out.txt', 'w') as out:
        for line in inf:
            if line.strip():
                out.write(line)


def ref_end():
    with open("out.txt", 'r') as out, open("res.txt", 'w') as res:
        for line in out:
            if line[-2].islower():
                #l = line.replace('\n', '')
                res.write(line.replace('\n', ''))
            elif line[-2] == ',':
                #l = line.replace('\n', '')
                res.write(line.replace('\n', ''))
            else:
                res.write(line)

def adding():
    with open("res.txt", 'r') as res, open("movie_lines.txt", 'w') as ml:
        i = 1
        for line in res:
            row = "+++$+++"
            o = int(i) % 2
            if o == 1:
                l = f"L{i} {row} u{o} {row} m13 {row} USERT {row} " + line
                ml.write(l)
                i += 1
            else:
                l = f"L{i} {row} u0 {row} m13 {row} USERO {row} " + line
                ml.write(l)
                i += 1

def ukrain():
    empry_line = "\n"
    with open("movie.txt", 'r') as mv, open("uk.txt", 'w') as uk:
        i = 1
        for line in mv:
            o = int(i) % 2
            if o == 1:
                uk.write("Iгор\n")
                uk.write(line)
                uk.write(empry_line)
                i+=1
            else:
                uk.write("Надя\n")
                uk.write(line)
                uk.write(empry_line)
                i+=1



if __name__== "__main__":
    # clear_time()
    # del_lines()
    # ref_end()
    # adding()
    ukrain()

