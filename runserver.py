import sys
import os
#----------------------------------------------------
if len(sys.argv)<2:
    print("Usage: {0} PORT".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)
port= sys.argv[1]
def main():
    try:
        os.system("python httpserver.py {0}".format(int(port)))
    except Exception as ex:
        print(ex, file= sys.stderr)
        sys.exit()
#---------------------------------------------------------
if __name__=="__main__":
    main()
        