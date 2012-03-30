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
def xor_chain(abyte="00000000", key=False, right2left=True, len=8):
	bytelist = list(abyte[::-1]) if (right2left) else list(abyte)
	hash = list()
	for i in range(len):
		#print(bytelist[i])
		bit = bool(int(bytelist[i]))
		#print("bit: " + str(bit))
		key = bit ^ key
		#print("key: " + str(key))
		hash.append(str(int(key)))
	#print("\n")
	return "".join(hash)

# convert byte (int from 0..255) to binary string
def byte_to_bin(rbyte=-1):
	# Generate random byte
	if (rbyte==-1):
		rbyte = random.randint(0,255)
	# format as binary string for output
	rbyte_str = "{0:08b}".format(rbyte)
	return rbyte_str
