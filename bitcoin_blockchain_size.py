from bitcoinrpc.authproxy import AuthServiceProxy
from pydash import at
import numpy as np
import matplotlib.pylab as plt
import time
import sys

JSON_username = "classified"
JSON_pass = "SUPER classified"

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332" % (JSON_username, JSON_pass))

genesis_block_hash = '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
blockchain_length = rpc_connection.getblockcount()
current_block = {}
current_total_size = 0
total_size = []
list = []

# parameters for iteration printing
digits = len(str(blockchain_length - 1))
delete = "\b" * digits


start_time = time.time()

for i in range(blockchain_length + 1):
    print("{0}{1:{2}}".format(delete, i, digits), end="")
    sys.stdout.flush()
    if i == 0:
        current_block_hash = genesis_block_hash
    else:
        current_block_hash = list[0]
    # [0] first elemnent in 'list': current block next hash
    # [1] second element in 'list': current block size
    list = at(rpc_connection.getblock(current_block_hash), 'nextblockhash', 'size')
    current_total_size += list[1]
    total_size.append(current_total_size)

x = np.arange(0, blockchain_length + 1, 1)
plt.plot(x, total_size)
plt.xlabel('block_number')
plt.ylabel('blockchain_size')
print("\nThe program took", time.time() - start_time, "seconds to run")
plt.show()
