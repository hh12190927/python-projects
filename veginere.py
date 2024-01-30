alphapets='abcdefghijklmnopqrstuvwxyz'
plaintext=input('Enter the Message: ').lower().replace(' ','')
key=input('Enter the key: ').lower().replace(' ','')
while len(plaintext)>len(key):
    key+=key
while len(plaintext)<len(key):
    key=key.replace(key[-1],'')
key+=' '
cipher_text=''
for i in range(len(plaintext)):
    cipher_text+=alphapets[(alphapets.index(plaintext[0])+alphapets.index(key[0]))%26]
    plaintext=plaintext.replace(plaintext[0],'')
    key=key.replace(key[0],'')
    print(key)
print(cipher_text)
