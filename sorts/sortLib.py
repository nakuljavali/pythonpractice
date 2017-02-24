import sys

def inputListStdin():
    for line in sys.stdin:
        ipList = line.split()
        return ipList

def inputListCli():
    sys.argv.pop(0)
    return map(int, sys.argv)
