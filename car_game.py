command=''
started=False

while True :
    command=input('> ').lower()
    counter=0
    counter2=0
    if command== 'start':
        if not started:
          started=True
          print('Car started... Ready to go!')
        else :
          print('Hey Car is already started !')

    elif command=='stop':
        if started:
          started=False
          print('Car stopped...')
        else:
          print('Car is already stopped..what are you doing?')
    elif command=='help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
 ''')
    elif command=='quit':
        break
    else :
        print("I don't understand that...")
    