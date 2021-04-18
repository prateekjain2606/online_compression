# Online compression of bits using LZ777 algorithm: Decoder
# compressed.txt is passed through the algorithm to obtain decompressed file has a binary representation.
# decompressed.txt is the decoded signal.

# To run the program, use the following command
# decoder.py decompressed.txt

import sys
import math

file_name = sys.argv[1]

f = open(file_name, "r")
Lines = f.readlines()

encode_list = []

search_length = int(sys.argv[2])
bin_len = math.ceil(math.log2(search_length))


for lines in Lines:
    start = int(lines[0: bin_len], 2)
    jump = int(lines[bin_len: 2 * bin_len], 2)
    ascii = chr(int(lines[2 * bin_len:2 * bin_len + 7], 2))
    encode_list.append([start, jump, ascii])


def Decode(encode_list):
    ans = ''
    for i in encode_list:
        offset, length, sym = i
        for j in range(length):
            ans += ans[-offset]
        ans += sym
    return ans


f = open("decompressed.txt", "w")
f.write(Decode(encode_list))
f.close
