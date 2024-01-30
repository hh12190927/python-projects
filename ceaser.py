def ceaser_cipher() :
    while True:
        try:
            En_De=input('Enter(E)for Encryption or(D)for decryption: ').lower()
            alphapet='abcdefghijklmnopqrstuvwxyz'
            plaintext=input('Enter the Message: ').lower().replace(' ','')
            key=int(input('Enter the key: '))
            ciphered_text=''
            for char in plaintext:
                if En_De=='e':
                    x= (alphapet.index(char)+key)%26
                elif En_De=='d':
                    x=(alphapet.index(char)-key)%26
                ciphered_text+=alphapet[x] 
        except :
            print('Invaild Value')
        print(ciphered_text)

ceaser_cipher()