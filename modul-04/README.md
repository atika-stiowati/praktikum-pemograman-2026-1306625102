# Modul [04] - [Grading]

**Nama:** [atika stiowati]  
**NIM:** [1306625102]  
**Kelas:** [fisika c]  

---

## 1. Problem Statement
> Problem Statement:
Pemrosesan data nilai dan penentuan predikat kelulusan (grading) mahasiswa secara manual dari file DataNilai.xlsx sangat rentan terhadap kesalahan. Tugas ini bertujuan membangun program berbasis Python di VS Code menggunakan print format, looping, list, dan counting untuk:   
JPEG
+ 1
Menghitung nilai akhir dengan rumus NA=30%(Lain-lain)+35%(UTS)+35%(UAS).   
JPEG
+ 1
Mengonversi nilai akhir menjadi grade (A sampai C, dan TL untuk < 56) berdasarkan standar institusi.   
JPEG
+ 1
Menampilkan tabel laporan nilai mahasiswa serta rekapitulasi jumlah mahasiswa per grade secara otomatis
## 2. Mathematical Equation
> 1. Persamaan Nilai Akhir (NA)
Nilai akhir mahasiswa dihitung menggunakan rata-rata terbobot dari tiga komponen penilaian:
   
JPEG
+ 1
NA=(0,30×Nilai Lain 
2
​	
 )+(0,35×Nilai UTS)+(0,35×Nilai UAS)
Dimana:
Nilai Lain 
2
​	
  = Komponen nilai tugas/aktivitas lain (bobot 30%)   
JPEG
+ 1
Nilai UTS = Nilai Ujian Tengah Semester (bobot 35%)   
JPEG
+ 1
Nilai UAS = Nilai Ujian Akhir Semester (bobot 35%)   
JPEG
+ 1
2. Persamaan Konversi Grade (Fungsi Bersyarat)
Nilai akhir (NA) dikonversi menjadi huruf mutu (grade) berdasarkan rentang nilai berikut:   
JPEG
+ 1
Grade= 
⎩

⎨

⎧
​	
  
A
A-
B+
B
B-
C+
C
TL
​	
  
jika 86≤NA≤100
jika 81≤NA<86
jika 76≤NA<81
jika 71≤NA<76
jika 66≤NA<71
jika 61≤NA<66
jika 56≤NA<61
jika NA<56
​	
 
   
JPEG
+ 1
3. Persamaan Penghitungan Rekapitulasi (Counting)
Untuk menghitung jumlah mahasiswa pada setiap kategori grade dan total keseluruhan mahasiswa, digunakan fungsi penjumlahan counter (c):
Jumlah Mahasiswa per Grade (N 
grade
​	
 ):
N 
grade
​	
 = 
i=1
∑
N
​	
 I(Grade 
i
​	
 ==Kategori)
(Dimana I adalah fungsi indikator bernilai 1 jika kondisi terpenuhi, dan 0 jika tidak).
Total Keseluruhan Mahasiswa (N 
total
​	
 ):
N 
total
​	
 =∑(N 
A
​	
 +N 
A-
​	
 +N 
B+
​	
 +N 
B
​	
 +N 
B-
​	
 +N 
C+
​	
 +N 
C
​	
 +N 
TL
​	
 )
## 3. Algorithm
> Algoritma Program Grading Mahasiswa

1. Mulai.
2. Masukkan identitas pembuat program, yaitu Nama dan NRM.
3. Inisialisasi variabel penghitung untuk setiap grade, yaitu count_A, count_A_min, count_B_plus, count_B, count_B_min, count_C_plus, count_C, dan count_TL dengan nilai awal 0.
4. Buat list kosong untuk menyimpan data mahasiswa.
5. Baca file Excel DataNilai.xlsx yang berisi data Mahasiswa, Nilai Lain2, Nilai UTS, dan Nilai UAS.
6. Lakukan perulangan untuk membaca setiap baris data mahasiswa dari file Excel.
7. Ambil data Nama Mahasiswa, Nilai Lain2, Nilai UTS, dan Nilai UAS.
8. Hitung Nilai Akhir (NA) dengan rumus:
    NA = (0.30 × Nilai Lain2) + (0.35 × Nilai UTS) + (0.35 × Nilai UAS)
9. Tentukan grade mahasiswa berdasarkan rentang Nilai Akhir, yaitu A, A-, B+, B, B-, C+, C, atau TL.
10. Tambahkan nilai penghitung sesuai dengan grade yang diperoleh mahasiswa.
11. Simpan data nomor, nama mahasiswa, nilai akhir, dan grade ke dalam list.
12. Ulangi langkah 7 sampai 11 hingga seluruh data mahasiswa selesai diproses.
13. Tampilkan identitas pembuat program, yaitu Nama dan NRM.
14. Tampilkan tabel hasil grading yang berisi nomor, nama mahasiswa, nilai akhir, dan grade.
15. Tampilkan rekapitulasi jumlah mahasiswa untuk setiap kategori grade.
16. Hitung dan tampilkan jumlah total seluruh mahasiswa.
17. Tampilkan tulisan Selesai.
18. Selesai.
