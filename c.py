key_list=['u','n','i','v','e','r','s','i','t','y']
matrix=[['m', 'o', 'h', 'a', 'e'],
         ['d', 'b', 'c', 'f', 'g'],
         ['i', 'j', 'kl', 'n', 'p'],
         ['q', 'r', 's', 't', 'u'],
         ['v', 'w', 'x', 'y', 'z']]
cypher_text=''
 
for s in range(int(float(len(key_list)/2))):#because i enter two letters each time
   print(key_list)
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
   if rowx==rowy:   
      cypher_text+=matrix[rowx][(columnx+1)%5]+matrix[rowy][(columny+1)%5]
   elif columnx==columny:
      cypher_text+=matrix[(rowx+1)%5][columnx]+matrix[(rowy+1)%5][columny]
   else :
      cypher_text+=matrix[rowx][columny]+matrix[rowy][columnx]
   del key_list[:2]
   x='';y=''

    
print(f'cypher text is: {cypher_text}')
    
   

    