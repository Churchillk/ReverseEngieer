import os
os.system("pip install capstone")
from capstone import Cs, CS_ARCH_X86, CS_MODE_32

# Replace the shellcode with your actual machine code
shellcode = b"\x8d\x4c\x32\x08\x01\xd8\x81\x78\x08\x64\x61\x74\x61\x75\xf4\x89\x74\x24\xfc"

# Initialize Capstone disassembler
md = Cs(CS_ARCH_X86, CS_MODE_32)

# Disassemble the machine code
for i in md.disasm(shellcode, 0x1000):
    print(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")
