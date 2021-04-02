#mengonversi nilai
#masukkan nama dan nilai
print('berikut adalah program untuk mengonversi nilai Anda')
x= str (input('siapa nama Anda?'))
y= float (input('berapa nilai anda?'))
info = 'halo,'+str( x )+'! nilai Anda setelah dikonversi adalah '
if y<60:
    print(info + ' E' )
elif 60<=y<=64:
    print(info+ 'C')
elif 65<=y<=69:
    print(info+ 'C+')
elif 70<=y<=74:
    print(info+ 'B')
elif 75<=y<=79:
    print(info+ 'B+')
elif 80<=y<=84:
    print(info+ 'A-')
elif 85<=y<=100:
    print (info+ 'A')
else:
    print('nilai tidak valid')

