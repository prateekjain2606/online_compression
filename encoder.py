# Online compression of bits using LZ777 algorithm: Encoder
# data.txt is passed through the algorithm to obtain compressed file and uncompressed file
# which has a binary representation. We obtain compressed.txt which is the compressed form
# of the given data. uncompressed.txt represents the binary representation of data without
# any compression.

# To run the program, use the following command
# encoder.py data.txt 15 10

import sys
import math

file_name = sys.argv[1]
search_buf_length = int(sys.argv[2])
look_ahead_buf_length = int(sys.argv[3])

f = open(file_name, "r")
str = f.read()
f.close()
buffer = ""
str_length = len(str)
search_buf_pos, look_ahead_buf_pos = 0, search_buf_length
encode_list = []

f = open("uncompressed.txt", "w")
for i in str:
    f.write(format(ord(i), "08b"))
    f.write("\n")
f.close()


def Init():
    global buffer
    buffer = str[search_buf_pos:search_buf_pos + search_buf_length]
    for i in buffer:
        encode_list.append([0, 0, i])
    buffer += str[look_ahead_buf_pos:look_ahead_buf_pos + look_ahead_buf_length]


def MoveForward(step):
    global search_buf_pos, look_ahead_buf_pos, buffer
    search_buf_pos += step
    look_ahead_buf_pos += step
    buffer = str[search_buf_pos:search_buf_pos + search_buf_length + look_ahead_buf_length]


def Encode():
    sym_offset = search_buf_length
    max_length, max_offset, next_sym = 0, 0, buffer[sym_offset]
    buffer_length = len(buffer)
    if buffer_length - sym_offset == 1:
        encode_list.append([0, 0, next_sym])
        return max_length
    for offset in range(1, search_buf_length + 1):
        pos = sym_offset - offset
        n = 0
        while buffer[pos + n] == buffer[sym_offset + n]:
            n += 1
            if n == buffer_length - search_buf_length - 1:
                break
        if max_length < n:
            max_length = n
            max_offset = offset
            next_sym = buffer[sym_offset + n]
    encode_list.append([max_offset, max_length, next_sym])
    return max_length


def LZ77():
    while 1:
        step = Encode() + 1
        MoveForward(step)
        if look_ahead_buf_pos >= str_length:
            break


Init()
LZ77()

f = open("compressed.txt", "w")

bin_len = math.ceil(math.log2(search_buf_length))
bin_len_1 = math.ceil(math.log2(search_buf_length))
for i in encode_list:
    temp = format(i[0], "016b")[16 - bin_len:16]
    temp = temp + format(i[1], "016b")[16 - bin_len:16]
    temp = temp + format(ord(i[2]), "08b")[1:8]
    f.write(temp)
    f.write("\n")
f.close()