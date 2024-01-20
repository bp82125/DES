from textwrap import wrap

from des import encrypt, decrypt
from utils import text_to_base64, base64_to_text


def DES_encrypt(plain_text, key):
    pt_base64 = text_to_base64(plain_text)
    key_base64 = text_to_base64(key)

    pt_parts = wrap(pt_base64, width=16)

    res = "".join([encrypt(part, key=key_base64) for part in pt_parts])

    return res


def DES_decrypt(cipher_text, key):
    key_base64 = text_to_base64(key)

    ct_parts = wrap(cipher_text, width=16)

    ori_hex = "".join([decrypt(part, key=key_base64) for part in ct_parts])
    plain_text = base64_to_text(ori_hex)
    return plain_text


if __name__ == "__main__":
    print("Enter the text for encryption: ")
    pt = input()
    print("Enter the key for encryption (8 characters length):")
    key = input()

    ct = DES_encrypt(pt, key)
    print(f"Cipher text: {ct}")

    ori_pt = DES_decrypt(ct, key)
    print(f"Original text: {ori_pt}")
