import os
import time
x = 0

def do():
    name = "code" + str(x+1) + ".py"
    myName = "code" + str(x) + ".py"
    try:
        fileC = open(name ,"x")
        fileW = open(name ,"w")
        fileR = open(myName, "r")
        for line in fileR:
            if line.startswith("x = "):
                fileW.write(f"x = {x+1}\n")
            elif line.startswith("        import code"):
                fileW.write(f"        import code{x+2}\n")
            elif line.startswith("        code"):
                fileW.write(f"        code{x+2}.do()\n")
            else:
                fileW.write(line)
        fileW.flush()
        fileW.close()
        import code1
        print(f"\033[1;32;40mFINISHED === \033[1;37;40m{myName}")
        time.sleep(2)
        code1.do()
    except Exception as identifier:
        print(f"\033[1;31;40mFAILED ===== \033[1;37;40m{myName}")
        print(f"\033[1;31;40m== {identifier}")