from collections import namedtuple

ProgramState = namedtuple('ProgramState', ['pc', 'halted', 'memory'])


def main():
    # load program
    program = load_program('02.txt')

    # part 1
    print('Part 1:')
    print(f'{execute_program(program, 12, 2)=}')

    # part 2
    solutions = [(noun, verb) for noun in range(100) for verb in range(100) if
                 execute_program(program, noun, verb) == 19690720]
    for noun, verb in solutions:
        print('Part 2:')
        print(f'{noun=}')
        print(f'{verb=}')
        print(f'{100 * noun + verb=}')


def load_program(program_path: str) -> ProgramState:
    with open(program_path) as f:
        program_text = f.read()
    memory = [int(value) for value in program_text.split(',')]
    return ProgramState(pc=0, halted=False, memory=memory)


def execute_program(program_state: ProgramState, noun: int, verb: int) -> int:
    state_stack = run(set_input(program_state, noun, verb),
                      lambda current: not current.halted,
                      update)
    return peek(state_stack).memory[0]


def run(initial, condition, step):
    stack = [initial]
    while condition(peek(stack)):
        stack.append(step(peek(stack)))
    return stack


def update(state):
    def binary_operation(operation):
        def perform(s):
            m = s.memory
            pc = s.pc
            a = m[pc + 1]
            b = m[pc + 2]
            c = m[pc + 3]
            m = set_memory(m, c, operation(m[a], m[b]))
            return ProgramState(pc=pc + 4, memory=m, halted=s.halted)

        return perform

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    def halt(s):
        return ProgramState(pc=s.pc, memory=s.memory, halted=True)

    if state.halted:
        raise Exception
    opcode = state.memory[state.pc]
    operations = {
        1:  binary_operation(add),
        2:  binary_operation(multiply),
        99: halt,
    }
    return operations[opcode](state)


def set_input(program_state, noun, verb):
    memory = set_memory(set_memory(program_state.memory, 1, noun), 2, verb)
    return ProgramState(pc=program_state.pc, halted=program_state.halted, memory=memory)


def set_memory(memory, position, value):
    return [*memory[:position], value, *memory[position + 1:]]


def peek(stack):
    return stack[-1]


if __name__ == '__main__':
    main()
