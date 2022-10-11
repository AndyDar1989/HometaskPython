# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a
# 1v2b2w2P3u2T1Y1y2W2Q
from fileinput import close
from os import path
from itertools import groupby, starmap


def rle_cod(data_name, rec_name):
    if path.exists(data_name) and not path.exists(rec_name):
        with open(data_name) as data_file,\
                open(rec_name, 'a') as rec_file:
            for i in data_file:
                rec_file.write(
                    ''.join([f"{len(list(count))}{chr}" for chr, count in groupby(i)]))
    else:
        print('path does not exist')


def unpack_data(data_name):
    with open(data_name) as data_file:
        data = data_file.read()
        i = 0
        while i < len(data):
            s_int = ''
            count = []
            chr = data[i]
            while chr.isdigit():
                s_int += chr
                i += 1
                if i < len(data):
                    chr = data[i]
                else:
                    break
            count.append([int(s_int), chr])
            print("".join(starmap(lambda x, y: x*y, count)), end='')
            i += 1


rle_cod('text_words.txt', 'text_code_words.txt')
unpack_data('text_code_words.txt')
