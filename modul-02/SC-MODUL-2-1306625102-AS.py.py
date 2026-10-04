print("Program Faktor Bilangan")
print("Nama : atika stiowati")
print("Nim : 1306625102")
print('\n')

while True:
    hasil= [25]
    n= int (input ('masukkan bilangan <100 (selesai)=0 '))
    if n ==0:
        break
    for i in range (1, n+1):
        if n % i == 0:
         hasil. append (i)
    print(' Bilangan faktor dari', n, 'adalah', hasil)
    print('selesai')
    
    
            