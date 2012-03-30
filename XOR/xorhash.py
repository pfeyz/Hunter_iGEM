##############################################################################
#
# Author: Daniel Packer <dp@danielpacker.org>
#
# Implements and tests an XOR hash function that takes a boolean key and 8bit 
# input to mimic the bacterial hash function found in the paper "Bacterial Hash 
# Function Using DNA-Based XOR Logic Reveals Unexpected Behavior of the LuxR 
# Promoter" -- http://www.ibc7.org/article/journal_v.php?sid=265
#

import random

# Run an xor chain on a given binary string with a given boolean key
# You can specify # of bits and direction in which to XOR the bitstring
def xor_chain(abyte="00000000", key=False, right2left=True, length=8):
	if right2left:
		abyte = abyte[::-1]
	xhash = list()
	for bit, _ in zip(abyte, range(length)):
		key = int(bit) ^ key
		xhash.append(str(key))
	return "".join(xhash)

# convert byte (int from 0..255) to binary string
def byte_to_bin(rbyte=None):
	# Generate random byte
	if rbyte is None:
		rbyte = random.randint(0,255)
	# format as binary string for output
	rbyte_str = "{0:08b}".format(rbyte)
	return rbyte_str
