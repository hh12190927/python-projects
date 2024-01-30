# import array
# a=array.array('i',[1,2,50])
# for i in a:
#     print(i,end=" ")
# def changeme( mylist ):
#     "This changes a passed list into this function"
#     mylist.append([1,2,3,4]);
#     print ("Values inside the function: ", mylist)
#     return
# # Now you can call changeme function
# mylist = [10,20,30];
# changeme( mylist );
# print ("Values outside the function: ", mylist)
def changeme( mylist ):
    "This changes a passed list into this function"
    mylist.append([1,2,3,4]); # This would assig new reference in mylist
    print ("Values inside the function: ", mylist)
    return
# Now you can call changeme function
x = [10,20,30];
changeme(x);
print ("Values outside the function: ", x)