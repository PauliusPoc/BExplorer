from bitcoin.rpc import RawProxy
from datetime import datetime
import sys

p = RawProxy()
block_hash = p.getblockhash(int(sys.argv[1]))
block = p.getblock(block_hash)
block_info = p.getblockstats(block_hash)

date_time = datetime.fromtimestamp(block['time'])

multiplier = 1e-8

result = [str(block['height']), block['hash'], block['previousblockhash'], str(date_time), str(block['confirmations']), str(block['nonce']), str(block_info['txs']), str(block_info['total_out']*multiplier) + " BTC", str(block_info['totalfee']*multiplier) + " BTC"]

print(result)
