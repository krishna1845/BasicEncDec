#encryption Function
def encrypt(msg, key):
  msg = list(msg)
  for i in range(len(msg)):
    msg[i] = chr(ord(msg[i]) + i + key)
  return "".join(msg)

#decryption Function
def decrypt(msg, key):
  msg = list(msg)
  for i in range(len(msg)):
    msg[i] = chr(ord(msg[i]) - i - key)
  return "".join(msg)

#main to take input
s = str(input("enter the message: "))
n = len(s)
key = input("enter key: ")
k = 0
for i in key:
  k += ord(i)

enc_msg = encrypt(s, k)
print("encrypted msg is \n" + enc_msg + "\n")
dec_msg = decrypt(enc_msg, k)
print("decrypted msg is \n" + dec_msg)
