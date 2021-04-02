#penggunaan if unruk tiga kasus dan selebihnya
# inputkan bilangan
print('masukkan koordinat!')
x= int (input('masukkan nilai x:'))
y= int (input('masukkan nilai y:'))
info= 'koordinat('+str(x)+','+str(y)+')berada pada kuadran'
#memeriksa nilai x dan y
if x>0 and y>0:
    print(info+'I')
elif x<0 and y>0:
    print(info + 'II')
elif x<0 and y<0:
    print (info+'III')
elif x>0 and y<0:
    print (info+'IV')
else:
    pass
print()

