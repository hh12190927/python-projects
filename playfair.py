

def playfair_cipher() :
    try:    
        alphapet='abcdefghijklmnopqrstuvwxyz'
        En_De=input('Enter(E)for Encryption or(D)for decryption: ').lower()
        plaintext=input('Enter the Message: ').lower().replace(' ','')
        print('What are the two letters that should be merged together?')
        key1 = input("First letter: ")
        key2 = input("Second letter: ")
        if (En_De=='e'):
         key=input('Enter the key: ').lower().replace(' ','')
        elif (En_De=='d'):
         key=input('Enter the cipher text: ').lower().replace(' ','')
        key_list=[]
        if len(key)%2!=0:
            key+=key[0]
        for u in range(len(key)):
            key_list.append(key[u])
        cipher_text=''
        matrix=[]
        row=[]
        v=''
        y=0
    #*******************************************************************************************************************   
        for char in plaintext:
            if char in matrix:
                continue
            matrix+=char
        for letter in alphapet:
            if letter not in plaintext :
                matrix+=letter
        if En_De=='d':
             key1=matrix[matrix.index(key1)+1]
             key2=matrix[matrix.index(key2)+1]
        if  key1 not in plaintext and key2 not in plaintext and key1!=key2 and (matrix.index(key1)==matrix.index(key2)-1):
                    matrix.remove(key2)
                    matrix.insert(matrix.index(key1),key1+key2)
                    matrix.remove(key1)
                    for i in range(5):
                        row=matrix[:5]
                        del matrix[:5]      
                        matrix.append(row)
                    print(matrix)
                    #print(key_list)
                    for s in range(int(float(len(key_list)/2))):#because i enter two letters each time
                        #print(key_list)
                        x,y=key_list[:2]
                        for row1 in range(5):
                            if x  not in matrix[row1] :
                                    continue
                            columnx=matrix[row1].index(x)
                            rowx=row1
                        for row2 in range(5):
                            if  y not in matrix[row2]:
                                    continue
                            columny=matrix[row2].index(y)
                            rowy=row2
                        if En_De=='e':
                            if rowx==rowy:   
                                cipher_text+=matrix[rowx][(columnx+1)%5]+matrix[rowy][(columny+1)%5]
                            elif columnx==columny:
                                cipher_text+=matrix[(rowx+1)%5][columnx]+matrix[(rowy+1)%5][columny]
                            else :
                                cipher_text+=matrix[rowx][columny]+matrix[rowy][columnx]
                            del key_list[:2]
                            x='';y=''
                        elif En_De=='d':
                            if rowx==rowy:   
                                cipher_text+=matrix[rowx][(columnx-1)%5]+matrix[rowy][(columny-1)%5]
                            elif columnx==columny:
                                cipher_text+=matrix[(rowx-1)%5][columnx]+matrix[(rowy-1)%5][columny]
                            else :
                                cipher_text+=matrix[rowx][columny]+matrix[rowy][columnx]
                            del key_list[:2]
                             
                    if key1+key2 in cipher_text:
                         cipher_text=cipher_text.replace(key1+key2,key1)  
                    if En_De=='e':                    
                        print(f'cipher code is :( {cipher_text} ))')                             
                    elif En_De=='d':                    
                        print(f'the key is( {cipher_text} ) or ( {cipher_text.replace(key1,key2)} )')                             
        else:
            print('please choose another two different letters to merge!')
    except:
          print("Error! Please enter letters in range a to z")
   #****************************************************************************************************************

playfair_cipher()