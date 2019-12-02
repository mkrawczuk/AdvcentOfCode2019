from common import InputForDay

indata = InputForDay(2).get()
indata[1] = 12
indata[2] = 2
op = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y
}

def program(code):
    ptr = 0
    while (99 != code[ptr]):
        opcode = code[ptr]
        op1 = code[1 + ptr]
        op2 = code[2 + ptr]
        op3 = code[3 + ptr]
        code[op3] = op[opcode](indata[op1], indata[op2])
        ptr += 4
        
    return code[0]


print("Part 1: {}".format(program(indata)))

# Part 2
noun = 0
verb = 0

incached = InputForDay(2).get()

# A very naive solution
for i in range(100):
    for j in range(100):
        if 19690720 == indata[0]:
            print("Part 2: {}".format(100 * noun + verb))
        indata = incached[:]
        indata[1] = i
        indata[2] = j
        program(indata)
        noun = i
        verb = j



