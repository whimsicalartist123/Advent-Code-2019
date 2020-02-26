
with open('data/integers.txt', 'r') as f:
    program = [int(x) for x in f.read().strip().split(',')]

def run_program(program):
    idx = 0

    while program[idx] != 99:
        opcode, p1, p2, res = program[idx:idx+4]
        if opcode == 1:
            program[res] = program[p1] + program[p2]
        elif opcode == 2:
            program[res] = program[p1] * program[p2]
        else:
            raise RuntimeError(f"invalid opcode: {program[idx]}")
        
        idx += 4
    
# run_program(program)
# print(program[0])

def run(program, noun, verb):
    memory = program[:]
    memory[1] = noun
    memory[2] = verb
    run_program(memory)
    return memory[0]

TARGET = 19690720

for noun in range(100):
    for verb in range(100):
        output = run(program, noun, verb)
        if output == TARGET:
            print(noun, verb, 100*noun + verb)