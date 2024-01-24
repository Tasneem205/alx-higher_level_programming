#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    if n < 1 :
        print("{} arguments".format(n))
    elif x == 1:
        print("{} arguments;".format(n))
    else:
        print("{} arguments;".format(x))
        for i in range(x):
            print("{}: {:s}".format(i+1, argv[i+1]))
