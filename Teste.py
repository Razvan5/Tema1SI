file = open("UserA.txt", "rb")
byte = file.read(16)
while byte:
    print(str(byte))
    byte = file.read(16)

# from Crypto.Cipher import AES
# # key1 = "1F61ECB5ED5D6BAF"
# key3 = "ABCDEFGH12345678"
# aes_test = AES.new(key3.encode(), AES.MODE_ECB)
# # print(aes_test.encrypt(key1.encode()))
# # print(aes_test.decrypt(b'*\xb6\x14\xfc\xefsb\n\xee\x80\xca\xbdk$T\xc5'))
#
#
# response = b"(b'\\xe6\\xa3|\\xf3\\x10\\xfd}\\x8f\\x89C\\x95\\xf0\\x1f;O\\xf2', b'\\xb7\\x89\\xa1)\\x95*I\\x84\\xb6\\xdfG\\x13q(!\\xdd')"
# response = str(response)
# print(response)
# encoded_key = response.split("(")[1].split(",")[0]
#
# x = encoded_key.replace('\\\\', '\\')
# print(x.encode().replace(b'\\\\', b'\\'))
# print(aes_test.decrypt(x.encode().replace(b'\\\\', b'\\')))
# print(aes_test.decrypt(b'\xe6\xa3|\xf3\x10\xfd}\x8f\x89C\x95\xf0\x1f;O\xf2'))
# print(aes_test.decrypt(b'\xb7\x89\xa1)\x95*I\x84\xb6\xdfG\x13q(!\xdd'))
# print(aes_test.decrypt(b'*\xb6\x14\xfc\xefsb\n\xee\x80\xca\xbdk$T\xc5'))

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


x = "1".encode()
y = "0".encode()
print(byte_xor(x,y))