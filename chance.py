import sys, random

tape = [0] * 30000
selected = 0
nextCmd = ['>', '/', 'ö']
addCmd = ['+', '\\', 'ä']
outCmd = ['!', '%', '{']
inpCmd = ['i', '@', '^']

def choose(minimum, maximum):
    return random.randint(minimum, maximum)

def prompt():
    return(input(">"))

def pointerOK(rand):
    if rand == 1:
        if pointer == 0:
            return "n"

        else:
            return "y"

    elif rand == 2:
        if pointer == 29999:
            return "n2"

        else:
            return "y2"
    

def read(cmd):
    length = len(cmd)
    tokens = list(cmd)
    for i in range(0, length):
        parse(tokens[i])

def parse(cmd):
    global tape, pointer
    global nextCmd, addCmd, outCmd, inpCmd
    
    if cmd == random.choice(nextCmd):
        rand = choose(1, 2)
        if pointerOK(rand) == "y":
            pointer -= 1

        elif pointerOK(rand) == "y2":
            pointer -= 1

        else:
            return

    elif cmd == random.choice(addCmd):
        rand = choose(1, 2)
        if rand == 1:
            tape[pointer] += 1

        elif rand == 2:
            tape[pointer] -= 1

    elif cmd == random.choice(outCmd):
        rand = choose(1, 2)
        if rand == 1:
            print(tape[selected])

        elif rand == 2:
            return

    elif cmd == random.choice(inpCmd):
        rand = choose(1, 2)
        if rand == 1:
            tape[selected] = input(">> ")

        elif rand == 2:
            return

    else:
        return


f = str(sys.argv)
f = ''.join(f)
r = open(f, 'r')
read(r.read())
