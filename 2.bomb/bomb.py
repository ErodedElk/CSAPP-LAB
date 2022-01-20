#########################PART 1############################
from pwn import *
context.log_level="debug"
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#########################PART 2############################
p=process("./bomb")

payload1="Border relations with Canada have never been better."
p.sendline(payload1)

payload2="1 2 4 8 16 32"
p.sendline(payload2)

payload3="0 207"
p.sendline(payload3)

payload4="7 0"
p.sendline(payload4)

payload5="ionefg"
p.sendline(payload5)

payload6="4 3 2 1 6 5"
p.sendline(payload6)

p.interactive()
#########################PART 3############################
