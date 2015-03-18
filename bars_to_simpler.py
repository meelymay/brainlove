import sys
if __name__ == '__main__':
    fname = sys.argv[1]
    f = open(fname, 'r')
    for line in f:
        fields = line.split(',')
        try:
            print fields[9],',',fields[0],fields[1],fields[10]
        except:
            pass
