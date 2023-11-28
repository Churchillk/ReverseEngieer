class SimpleInterpreter:
    def __init__(self):
        self.registers = {'eax': 0, 'ebx': 0, 'ecx': 0, 'edx': 0}

    def interpret_instruction(self, instruction):
        parts = instruction.split()
        if len(parts) < 2:
            print("Invalid instruction format.")
            return

        opcode = parts[0]
        operands = parts[1:]

        if opcode == 'mov':
            self.execute_mov(operands)
        else:
            print(f"Unsupported opcode: {opcode}")

    def execute_mov(self, operands):
        if len(operands) != 2:
            print("Invalid 'mov' instruction format.")
            return

        dest, src = operands
        if dest not in self.registers:
            print(f"Invalid destination register: {dest}")
            return

        if src.isdigit():
            self.registers[dest] = int(src)
        elif src in self.registers:
            self.registers[dest] = self.registers[src]
        else:
            print(f"Invalid source operand: {src}")

    def print_registers(self):
        print("Registers:")
        for reg, value in self.registers.items():
            print(f"{reg}: {value}")

def main():
    interpreter = SimpleInterpreter()

    while True:
        user_input = input("Enter machine code instruction (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break

        interpreter.interpret_instruction(user_input)
        interpreter.print_registers()

if __name__ == "__main__":
    main()
