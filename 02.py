from collections import namedtuple

ProgramState = namedtuple('ProgramState', ['pc', 'halted', 'registers'])


def main():
    with open('02.txt') as f:
        code = f.read()
    registers = [int(value) for value in code.split(',')]
    initialized_registers = alarm_1202(registers)
    initial_state = ProgramState(pc=0, halted=False, registers=initialized_registers)
    state_stack = run(initial_state,
                      lambda current: not current.halted,
                      update)

    print(f'Part 1: {peek(state_stack).registers[0]}')
    print('state_stack:')
    print('\n'.join(str(state) for state in state_stack))


def alarm_1202(registers):
    return set_register(set_register(registers, 1, 12), 2, 2)


def set_register(registers, position, value):
    return [*registers[:position], value, *registers[position + 1:]]


def run(initial, condition, step):
    stack = [initial]
    while condition(peek(stack)):
        stack.append(step(peek(stack)))
    return stack


def peek(stack):
    return stack[-1]


def update(state):
    def binary_operation(operation):
        def perform(s):
            r = s.registers
            pc = s.pc
            a = r[pc + 1]
            b = r[pc + 2]
            c = r[pc + 3]
            r = set_register(r, c, operation(r[a], r[b]))
            return ProgramState(pc=pc + 4, registers=r, halted=s.halted)

        return perform

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    def halt(s):
        return ProgramState(pc=s.pc, registers=s.registers, halted=True)

    if state.halted:
        raise Exception
    opcode = state.registers[state.pc]
    operations = {
        1: binary_operation(add),
        2: binary_operation(multiply),
        99: halt,
    }
    return operations[opcode](state)


if __name__ == '__main__':
    main()
