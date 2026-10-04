# Modul [03] - [Trigonometric with function]

**Nama:** [Atika Stiowati]  
**NIM:** [1306625102]  
**Kelas:** [Fisika c]  

---

## 1. Problem Statement
> Membuat sebuah program untuk menghitung nilai sinus dan cosinus dengan menggunakan pendekatan deret Mc Laurin

## 2. Mathematical Equation
> a. Deret Mc Laurin untuk sinus:
> \sin x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!}x^{(2n+1)}
> b. Deret Mc Laurin untuk cos:
> \cos x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!}x^{(2n)}
> c. Rumus Relative Error (ER) :
> Er = \left|\frac{AV-TV}{TV}\right| \times 100\%

## 3. Algorithm
> 1. Mulai program.
> 2. Import library math.
> 3. Masukkan nilai sudut dalam derajat.
> 4. Konversikan sudut dari derajat ke radian.
> 5. Hitung nilai sin menggunakan deret McLaurin:
   sin(x) = x - (x^3/3!) + (x^5/5!) - (x^7/7!) + ...
> 6. Hitung nilai cos menggunakan deret McLaurin:
   cos(x) = 1 - (x^2/2!) + (x^4/4!) - (x^6/6!) + ...
> 7. Hitung nilai sin dan cos menggunakan fungsi math sebagai True Value (TV).
> 8. Hitung Relative Error (Er) menggunakan rumus:
   Er = |(AV - TV) / TV| x 100%
> 9. Periksa apakah Relative Error sudah kurang dari 5%.
> 10. Jika Er belum kurang dari 5%, tambahkan jumlah suku deret dan ulangi perhitungan.
> 11. Jika Er sudah kurang dari 5%, tampilkan hasil nilai sin, cos, dan Relative Error.
> 12. Selesai.
