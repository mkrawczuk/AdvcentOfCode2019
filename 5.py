from common import InputForDay

indata = InputForDay(5).get()

iptr = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
}

def parseInstruction(instr: int):
    # Integer -> list of digits
    instr = [int(x) for x in str(instr)]
    # Add leading zeros and return
    return [0]*(5-len(instr)) + instr

# TODO: refactor the Intcode computer representation below.
# It will sure be useful in further tasks.
def program(code):
    ptr = 0
    while (99 != code[ptr]):
        increment = True
        # Parse instruction
        instr = parseInstruction(code[ptr])
        op = instr[-1]
        arg1mode = instr[-3]
        arg2mode = instr[-4]
        # arg3mode = instr[-5]
        arg3 = code[ptr + 3]
        # Execute instruction
        if (1 == op):
            # Get arg 1
            if arg1mode == 0:
                arg1 = code[code[ptr + 1]]
            elif arg1mode == 1:
                arg1 = code[ptr + 1]
            else:
                raise Exception("Something went wrong.")
            
            # Get arg 2
            if arg2mode == 0:
                arg2 = code[code[ptr + 2]]
            elif arg2mode == 1:
                arg2 = code[ptr + 2]
            else:
                raise Exception("Something went wrong.")

            code[arg3] = arg1 + arg2

        elif (2 == op):
            # Get arg 1
            if arg1mode == 0:
                arg1 = code[code[ptr + 1]]
            elif arg1mode == 1:
                arg1 = code[ptr + 1]
            else:
                raise Exception("Something went wrong.")
            
            # Get arg 2
            if arg2mode == 0:
                arg2 = code[code[ptr + 2]]
            elif arg2mode == 1:
                arg2 = code[ptr + 2]
            else:
                raise Exception("Something went wrong.")

            code[arg3] = arg1 * arg2

        elif (3 == op):
            code[code[ptr + 1]] = int(input("System ID: "))

        elif (4 == op):
            print(code[code[ptr+1]])

        elif (5 == op):
            # Get arg 1
            if arg1mode == 0:
                arg1 = code[code[ptr + 1]]
            elif arg1mode == 1:
                arg1 = code[ptr + 1]
            else:
                raise Exception("Something went wrong.")
            
            # Get arg 2
            if arg2mode == 0:
                arg2 = code[code[ptr + 2]]
            elif arg2mode == 1:
                arg2 = code[ptr + 2]
            else:
                raise Exception("Something went wrong.")

            if (0 != arg1):
                ptr = arg2
                increment = False

        elif (6 == op):
            # Get arg 1
            if arg1mode == 0:
                arg1 = code[code[ptr + 1]]
            elif arg1mode == 1:
                arg1 = code[ptr + 1]
            else:
                raise Exception("Something went wrong.")
            
            # Get arg 2
            if arg2mode == 0:
                arg2 = code[code[ptr + 2]]
            elif arg2mode == 1:
                arg2 = code[ptr + 2]
            else:
                raise Exception("Something went wrong.")

            if (0 == arg1):
                increment = False
                ptr = arg2

        elif (7 == op):
            # Get arg 1
            if arg1mode == 0:
                arg1 = code[code[ptr + 1]]
            elif arg1mode == 1:
                arg1 = code[ptr + 1]
            else:
                raise Exception("Something went wrong.")
            
            # Get arg 2
            if arg2mode == 0:
                arg2 = code[code[ptr + 2]]
            elif arg2mode == 1:
                arg2 = code[ptr + 2]
            else:
                raise Exception("Something went wrong.")

            if (arg1 < arg2):
                code[arg3] = 1
            else:
                code[arg3] = 0

        elif (8 == op):
            # Get arg 1
            if arg1mode == 0:
                arg1 = code[code[ptr + 1]]
            elif arg1mode == 1:
                arg1 = code[ptr + 1]
            else:
                raise Exception("Something went wrong.")
            
            # Get arg 2
            if arg2mode == 0:
                arg2 = code[code[ptr + 2]]
            elif arg2mode == 1:
                arg2 = code[ptr + 2]
            else:
                raise Exception("Something went wrong.")

            if (arg1 == arg2):
                code[arg3] = 1
            else:
                code[arg3] = 0

        else:
           raise Exception("Something went wrong.") 
        # Increment instruction pointer
        if (increment):
            ptr += iptr[op]
        
    return code[0]

program(indata)
