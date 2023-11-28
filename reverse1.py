from capstone import Cs, CS_ARCH_X86, CS_MODE_32

def disassemble_user_input(shellcode):
    # Initialize Capstone disassembler
    md = Cs(CS_ARCH_X86, CS_MODE_32)

    # Disassemble the user-provided machine code
    for i in md.disasm(shellcode, 0x1000):
        print(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")

def main():
    # Receive a byte input from the user
    user_input_hex = input("Enter the shellcode in hexadecimal format: ")

    # Convert the hexadecimal string to bytes
    try:
        shellcode = bytes.fromhex(user_input_hex)
    except ValueError:
        print("Invalid input. Please enter a valid hexadecimal string.")
        return

    # Disassemble the user-provided machine code
    disassemble_user_input(shellcode)

if __name__ == "__main__":
    main()
