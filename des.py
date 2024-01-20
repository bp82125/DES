from collections import namedtuple
from textwrap import wrap

from const import key_parity, shift_table, key_compression, initial_table, expansion_table, sub_boxes, final_sbox_table, \
    final_table
from utils import hex2bin, permute, shift_left, xor, bin2dec, bin2hex, dec2bin

round_key_pairs = namedtuple('RoundKey', ['round_key_bin', 'round_key_hex'])


def round_key(key):
    bin_key_64 = hex2bin(key)
    bin_key_56 = permute(bin_key_64, key_parity, 56)

    left = bin_key_56[0:28]
    right = bin_key_56[28:56]

    round_key_table = []

    for i in range(0, 16):
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])

        res = left + right

        bin_key_48 = permute(res, key_compression, 48)
        hex_key_48 = bin2hex(bin_key_48)

        round_key_table.append(round_key_pairs(round_key_bin=bin_key_48, round_key_hex=hex_key_48))

    return round_key_table


def sbox_conversion(bin_key_48):
    sub_strs = wrap(bin_key_48, width=6)

    res = ""
    for i, substr in enumerate(sub_strs):
        col = bin2dec(substr[1:5])
        row = bin2dec(substr[0] + substr[-1])

        res += dec2bin(sub_boxes[i][row][col])

    return res


def encrypt(plain_text, key=None, rk_table=None):
    if rk_table is None:
        round_k_table = round_key(key)
    else:
        round_k_table = rk_table

    bin_pt_64 = hex2bin(plain_text)
    bin_pt_64 = permute(bin_pt_64, initial_table, 64)

    left = bin_pt_64[0:32]
    right = bin_pt_64[32:64]

    for i in range(0, 16):
        right_expanded = permute(right, expansion_table, 48)
        round_key_xor_right = xor(right_expanded, round_k_table[i].round_key_bin)

        sbox_val = sbox_conversion(round_key_xor_right)
        sbox_val = permute(sbox_val, final_sbox_table, 32)

        res = xor(left, sbox_val)
        left = res

        if i != 15:
            left, right = right, left

    combine = left + right
    final = permute(combine, final_table, 64)
    return bin2hex(final)


def decrypt(cipher_text, key):
    round_key_table = round_key(key)
    round_key_table = round_key_table[::-1]
    return encrypt(cipher_text, rk_table=round_key_table)


if __name__ == "__main__":
    text = "123456ABCD132536"
    key_hex = "AABB09182736CCDD"
    encrypted_text = "C0B7A8D05F3A829C"

    print(f'Decrypt text: {bin2hex(decrypt(encrypted_text, key_hex))}')
