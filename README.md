# Tubes-TBFO-2021
 
 ## Anggota

| NIM      | NAMA                         |
|----------|----------------------------- |
| 13520134 | Raka Wirabuana Ninagan       |
| 13520151 | Rizky Ramadhana P. K.        |
| 13520155 | Jundan Haris                 |

## Deskripsi Singkat

Dalam penulisan sebuah source code, perlu diperiksa apakah ekspresi tersebut legal atau tidak. Legal atau tidaknya sebuah ekspresi diatur menurut sebuah aturan yang berbeda di tiap-tiap bahasa pemrograman. Aturan tersebut dapat dikodifikasi dalam sebuah Context Free Grammar (CFG). Lalu untuk menentukan apakah suatu input memenuhi suatu aturan, dilakukan parsing dengan menggunakan algoritma Cocke-Young-Kasami (CYK). Program ini akan mensimulasikan pengecekan syntax pada source code bahasa Python berdasar grammar yang telah dibuat pada file grammar.txt

## Cara Penggunaan

1. Clone repository ini pada laptop atau komputer Anda
2. Masuk ke folder Tubes-TBFO-2021
3. Pastikan bahwa grammar sudah terkonversi ke dalam bentuk CNF dengan melakukan konversi menggunakan perintah berikut. "grammar.txt" dapat diganti dengan sembarang nama file yang mengandung CFG yang diinginkan
'''
python cfg_to_cnf.py grammar.txt
'''
4. Grammar dalam bentuk CNF akan tersimpan dalam file 'chomsky'
5. Jalankan perintah "python main.py" lalu Anda akan diminta nama file apa yang ingin kebenaran syntaxnya. Contoh : testcase/tc3.py
6. Program akan melakukan parsing berdasar grammar yang diberikan dan menentukan apakah input valid atau tidak
