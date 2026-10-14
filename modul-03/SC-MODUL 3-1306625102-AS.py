import math

def mclaurin_sin(x, k):
    n = k - 1
    return ((-1)**n) * (x**(2*n+1)) / math.factorial(2*n+1)

def mclaurin_cos(x, k):
    n = k - 1
    return ((-1)**n) * (x**(2*n)) / math.factorial(2*n)

def tabel():
    ulang = "y"
    while ulang.lower() == "y":
        print("\n" + "=" * 65)
        print("Program Sinus-Cosinus (Deret Maclaurin)")
        print("Nama : Atika Stiowati")
        print("NIM  : 1306625102")
        print("=" * 65)

        sudut_deg = float(input("Besar sudut (dalam derajat): "))
        x_rad = math.radians(sudut_deg)

        tv_sin = math.sin(x_rad)
        tv_cos = math.cos(x_rad)

        print(f"\nTrue value sin({sudut_deg}°) = {tv_sin:.6f}")
        print(f"True value cos({sudut_deg}°) = {tv_cos:.6f}\n")

        # Cetak Header Tabel
        print("-" * 65)
        print(f"{'Suku':^7} | {'Appx Sin':^12} | {'Err Sin (%)':^11} | {'Appx Cos':^12} | {'Err Cos (%)':^11}")
        print("-" * 65)

        suku = 1
        av_sin = 0.0
        av_cos = 0.0

        while True:
            # Menggunakan fungsi Maclaurin yang sudah didefinisikan sebelumnya
            term_sin = mclaurin_sin(x_rad, suku)
            term_cos = mclaurin_cos(x_rad, suku)

            av_sin += term_sin
            av_cos += term_cos

            er_sin = abs((av_sin - tv_sin) / tv_sin) * 100 if tv_sin != 0 else 0.0
            er_cos = abs((av_cos - tv_cos) / tv_cos) * 100 if tv_cos != 0 else 0.0

            print(f"{suku:^7} | {av_sin:^12.6f} | {er_sin:^11.2f} | {av_cos:^12.6f} | {er_cos:^11.2f}")

            # Kondisi berhenti jika kedua relatif error < 5%
            if er_sin < 5 and er_cos < 5:
                break

            suku += 1

        print("-" * 65)
        ulang = input("\nApakah Anda ingin mengulang program? (y/t): ")

tabel()
print("\nSelesai")