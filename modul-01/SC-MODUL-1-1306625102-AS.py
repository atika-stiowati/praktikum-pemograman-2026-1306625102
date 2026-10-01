print("pemograman konversi suhu")
print(" nama : atika stiowati")
print(" nim : 1306625102")
print()

x = int(input("suhu_awal :"))
y = int(input("suhu_akhir :"))
z = int(input("selang :"))
print()

print("TABEL KONVENSI")
print()
print('-' * 56)
print("| {0:^5}|{1:^15}|{2:^15}|{3:^15}|".format('no','Celcius', 'Fahrenheit', 'Reamur'))
print('-' * 56)

n=1
while (x<= y):
    C = round(x)
    R = round((4/5) * C)
    F = round((9/5) * C + 32)
    print("|{0:^5}|{1:^15}|{2:^15}|{3:^15}|".format(n,C,R,F))
    n=n+1
    x=x+z

print('=' \
'' * 56)

print()
print("selesai")

