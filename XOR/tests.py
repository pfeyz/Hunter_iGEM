import collections
import itertools
import unittest

from xorhash import xor_chain, byte_to_bin
from xorhashobj import hasher, IncompleteHashError

class HashTest(unittest.TestCase):

    # test_strings tuple format:
    # (input bytestring, output with no args, output with key=True,
    #  output with len=6, output with key=True and len=3)
    test_strings = (
        ("11000110", "01000010", "10111101", "010000", "101"),
        ("11010100", "00110010", "11001101", "001100", "110"),
        ("01101111", "10100100", "01011011", "101001", "010"),
        ("00010101", "11001111", "00110000", "110011", "001"),
        ("11110110", "01001010", "10110101", "010010", "101"),
        ("11100111", "10111010", "01000101", "101110", "010"),
        ("11001100", "00100010", "11011101", "001000", "110"),
        ("01000001", "11111100", "00000011", "111111", "000"),
        ("00111000", "00010111", "11101000", "000101", "111"),
        ("10110101", "11001001", "00110110", "110010", "001"))

    def test_xor_chain(self):
        for bytestr, noargs, keyT, len6, keyTlen3 in HashTest.test_strings:
            self.assertEquals(xor_chain(bytestr), noargs)
            self.assertEquals(xor_chain(bytestr, key=True), keyT)
            self.assertEquals(xor_chain(bytestr, length=6), len6)
            self.assertEquals(xor_chain(bytestr, key=True, length=3), keyTlen3)

    def test_hasher(self):
        for bytestr, _, keyT, _, _, in HashTest.test_strings:
            x = hasher(bytestr, True, True, 8)
            i=0
            result = ""
            while (x.step()):
                i+=1
                result += str(int(x.output()))
            self.assertEquals(result, keyT)
            self.assertEquals("".join(x.hash), keyT)

            x.reset()

            i=0
            result = ""
            while (x.step()):
                i+=1
                result += str(int(x.output()))
            self.assertEquals(result, keyT, "Hasher failed after reset")
            self.assertEquals("".join(x.hash), keyT, "Hasher failed after reset")

            x.reset()
            for i in range(8):
                self.assertRaises(IncompleteHashError, lambda: x.hash)
                x.step()

    def test_hash_collisions(self):
        keyvals = {}
        for b, d in itertools.product([True, False], [True, False]):
            for i in range(255):
                bstr = byte_to_bin(i)
                keyvals[bstr] = xor_chain(bstr, b, d)
            c = collections.Counter(keyvals.values())
            duplicates = [i for i in c if c[i]>1]
            self.assertEquals(0, len(duplicates),
                              ("duplicates found: {0}."
                              "# originals: {1}, # duplicates {2}").format(
                                  duplicates,
                                  len(duplicates),
                                  len(keyvals.values())))

if __name__ == "__main__":
    import unittest
    unittest.main()
