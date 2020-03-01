# """
# Opcode:
#     1. 
#     2. 
#     3. Take input from use and put in position given
#     4. Output value at address given.

# Parameter mode
#     0 - Position mode: parameter treated as position in the input.
#     1 - immediate mode: parameter treated as value.

# """
with open('data/day5.txt', 'r') as f:
    program = [int(x) for x in f.read().strip().split(',')]

def parse_opcode(num):
    opcode = num % 100

    c = (num // 100) % 10
    b = (num // 1000) % 10
    a = (num // 10000) % 10
    # print(opcode, p1_mode, p2_mode, p3_mode)
    return opcode, (c, b, a)

def act(memory, modes, idx):
    
    val1 = memory[idx+1] if modes[0] == 0 else idx+1
    val2 = memory[idx+2] if modes[1] == 0 else idx+2
    return val1, val2

def run_program(program):
    memory = program[:]
    idx = 0
    output = []
    while memory[idx] != 99:

        opcode, modes = parse_opcode(memory[idx])
        if opcode == 1:
            # print(f"Opcode: {opcode}\t")
            val1, val2 = act(memory, modes, idx)
            memory[memory[idx+3]] = memory[val1] + memory[val2]
            idx += 4
        elif opcode == 2:
            val1, val2 = act(memory, modes, idx)
            memory[memory[idx+3]] = memory[val1] * memory[val2]
            idx += 4
        elif opcode == 3:
            addr = memory[idx + 1]
            x = int(input("Enter input: "))
            memory[addr] = x
            idx += 2
        elif opcode == 4:
            val = memory[idx+1] if modes[0] == 0 else idx+1
            output.append(memory[val])
            idx += 2
        else:
            raise RuntimeError(f"invalid opcode: {memory[idx]}")
    return output

print(run_program(program))
# # parse_opcode(4)
# print(program.count(4))

