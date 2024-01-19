hex2bin_table = {'0': "0000",
                 '1': "0001",
                 '2': "0010",
                 '3': "0011",
                 '4': "0100",
                 '5': "0101",
                 '6': "0110",
                 '7': "0111",
                 '8': "1000",
                 '9': "1001",
                 'A': "1010",
                 'B': "1011",
                 'C': "1100",
                 'D': "1101",
                 'E': "1110",
                 'F': "1111"}

bin2hex_table = {"0000": '0',
                 "0001": '1',
                 "0010": '2',
                 "0011": '3',
                 "0100": '4',
                 "0101": '5',
                 "0110": '6',
                 "0111": '7',
                 "1000": '8',
                 "1001": '9',
                 "1010": 'A',
                 "1011": 'B',
                 "1100": 'C',
                 "1101": 'D',
                 "1110": 'E',
                 "1111": 'F'}


def hex2bin(s: str) -> str:
    return "".join([hex2bin_table[ch] for ch in s])


def bin2hex(s: str) -> str:
    temp = []
    for i in range(0, len(s), 4):
        temp.append(s[i:i + 4])

    return "".join([bin2hex_table[substr] for substr in temp])


def bin2dec(s: str) -> int:
    return int(s, 2)


def dec2bin(n: int) -> str:
    bin_str = bin(n)[2:]
    zero2add = (4 - (len(bin_str) % 4)) % 4

    return "0" * zero2add + bin_str


def permute(s, table, base):
    return "".join([s[table[i] - 1] for i in range(0, base)])


def xor(s1: str, s2: str) -> str:
    return "".join([str(int(s1[i]) ^ int(s2[i])) for i in range(len(s1))])


def shift_left(s, offset) -> str:
    offset = offset % len(s)
    return s[offset:] + s[:offset]


if __name__ == "__main__":
    print(shift_left("00001111", 5))
