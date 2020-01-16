from bitcoin.rpc import RawProxy
from datetime import datetime

p = RawProxy()

latest_block_height = p.getblockcount()
latest_blocks = []
multiplier = 1e-8

for i in range(0, 10):
	block_hash = p.getblockhash(latest_block_height - i)
	block = p.getblock(block_hash)
	block_info = p.getblockstats(block_hash)
	date_time = datetime.fromtimestamp(block['time'])
	result = [str(block['height']), block_hash, str(date_time), str((block_info['subsidy'] + block_info['totalfee'])*multiplier) + " BTC"]
	latest_blocks.append(result)

print(latest_blocks)