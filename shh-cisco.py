#!/opt/local/bin/python
import hashlib
import Exscript

from Exscript.util.interact import read_login
from Exscript.protocols import SSH2

account = read_login()                    # Prompt the user for his name and password
conn = SSH2()                                    # We choose to use SSH2
conn.connect('192.168.16.1')        # Open the SSH connection
conn.login(account)                         # Authenticate on the remote host
conn.execute('conf t')                     # Execute the "uname -a" command
conn.execute('interface Fastethernet 0/8')
conn.execute('Description Test*')
conn.execute('no shutdown')
conn.execute('end')
conn.execute('sh run int Fastethernet0/8')
print conn.response

