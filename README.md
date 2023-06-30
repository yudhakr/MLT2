# Laporan Machine Learning Terapan - Ayudha Kusuma R.
## Submission MLT2 -Dicoding
Judul Proyek : Sistem Rekomendasi Kursus Online Pada Udemy Courses

![3](https://github.com/yudhakr/MLT2/assets/84507343/4fd6b452-bf61-43ca-af3a-4513e20c6bcd)

## Project Overview
  Udemy adalah sebuah platform pembelajaran online yang menyediakan ribuan kursus yang dapat diakses oleh siapa saja. Didirikan pada tahun 2010, Udemy memungkinkan instruktur atau ahli di berbagai bidang untuk membuat dan mengajarkan kursus-kursus mereka kepada para pelajar di seluruh dunia.
Kursus-kursus di Udemy mencakup beragam topik, termasuk ilmu komputer, bisnis, keuangan, seni dan desain, bahasa, musik, fotografi, pengembangan pribadi, dan banyak lagi.

  Pada Proyek ini membuat Sistem Rekomendasi Kursus Online Pada Udemy Courses, dimana banyak sekali pengguna maupun user yang mencari kelas tertentu dengan kireteria tertentu.Banyak pengguna yang baru memasuki bidang tertentu memilih untuk belajar melalui kursus online. Namun, dengan banyaknya pilihan kursus yang tersedia, sering kali mereka merasa kebingungan dalam memilih kursus selanjutnya. Untuk mengatasi hal ini, diperlukan adanya sebuah sistem rekomendasi yang dapat membantu pengguna baru menemukan kursus online yang sesuai dengan minat dan kebutuhan mereka. Sistem rekomendasi ini tidak hanya berfungsi sebagai sarana periklanan, tetapi juga dapat meningkatkan popularitas kursus online yang baru atau kurang terkenal, karena sebelumnya sulit untuk ditemukan. Dengan adanya sistem rekomendasi, pengguna dapat dengan mudah menemukan kursus yang mereka harapkan dan memperluas pengetahuan mereka dalam bidang yang diminati. [1]

## Business Understanding
### Problem Statements
 Berdasarkan masalah diatas maka dapat ditarik suatu rumusan masalah yaitu:
 - Sistem rekomendasi apa yang cocok dalam penerapan kasus proyek ini ?
 - Bagaimana cara membuat sistem rekomendasi kursus online pada Udemy Courses
   
### Goals
Berikut tujuan dari proyek ini:
- Membuat sistem rekomendasi kursus online untuk pengguna di Udemy.
- Memberikan rekomendasi untuk kursus online Udemy berdasarkan kriteria yang diinginkan pengguna.
- Memberikan remoendasi kelas berdasarkan bidang yang diminati.

### Solution Approach

Solusi yang dapat dilakukan untuk mencapai tujuan proyek ini diantaranya:
- Untuk pra-pemrosesan data dilakukan beberapa teknik diantaranya:
  - Membersihkan data duplikasi.
  - Membersihkan teks judul pada kolom course_title dari stopwords.
  - Membersihkan teks judul pada kolom course_title dari karakter spesial.

  Visualisasi data dapat dilihat lebih lengkap di bagian _Data Understanding_.

- Untuk persiapan data (sebelum dimasukkan ke model) dilakukan Vektorisasi menggunakan _TF-IDF Vectorizer_ untuk ekstraksi fitur pada teks judul kursus.

- Pembuatan sistem rekomendasi dilakukan dengan pendekatan _content-based filtering_ berdasarkan dataset yang ada. Sehingga sistem rekomendasi dibuat untuk memberikan rekomendasi pada pengguna terhadap kursus online yang sebelumnya diikuti/dibeli. Beberapa algoritma yang digunakan untuk membuat sistem rekomendasi di proyek ini diantaranya:
  - Sistem rekomendasi berbasis model, yakni dengan algoritma K-Nearest Neighbor. Algoritma tersebut dipilih karena lebih mudah diaplikasikan dan cukup sesuai untuk kasus klasterisasi di sistem rekomendasi. Algoritma ini berasumsi bahwa suatu data yang serupa memiliki kedekatan. Cara kerja dari algoritma ini adalah sebagai berikut (diterjemahkan dari [[3](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)]):
    - Muat datanya.
    - Inisialisasi nilai K (banyak tetangga/kelompok).
    - Pada setiap data:
      - Hitung _euclidean distance_ antara kueri yang diberikan dan contoh yang ada pada data tersebut dengan rumus berikut:
        $$d(xi, x1) = √(x₁ − xu)² + (xi2 − X12)² + ... + (Tip − Xlp) $$
      - Tambahkan jarak dan urutan dari contoh pada koleksi yang berurutan.
    - Pilih entri K paling awal pada koleksi yang berurutan.
    - Dapatkan label dari entri K yang dipilih.
    - Apabila kasus regresi, kembalikan nilai rata-ratanya. Apabila kasus klasifikasi, kembalikan nilai labelnya.

    Algoritma ini digunakan karena memiliki kelebihan dan kekurangan sebagai berikut (diterjemahkan dari [[3](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)]):
    - Kelebihan:
      - Algoritma yang mudah digunakan dan sederhana.
      - Algoritma yang sangat fleksibel, dapat diimplementasikan pada kasus klasifikasi, regresi dan pencarian.
    - Kekurangan:
      - Algoritmanya menjadi lebih lambat secara signifikan karena jumlah sampel/contoh dan/atau prediktor/variabel yang meningkat.

  - Sistem rekomendasi berbasis algoritma _cosine similarity_. Algoritma ini dipilih karena relatif mudah digunakan dan digunakan sebagai pembanding sistem rekomendasi yang menggunakan model. _Cosine similarity_ secara singkat, digunakan untuk mengukur kemiripan antara dua buah vektor dan kesamaan arahnya dengan cara menghitung nilai sudut kosinus dari kedua vektor. Rumus yang digunakan sebagai berikut:

 $$ k(v1, v2) = (v1 . v2) / ||v1|| ||v2|| $$

dimana :
- v1 dan v2 adalah vektor yang akan dibandingkan.
- (v1 . v2) adalah hasil perkalian dot product antara vektor A dan B.
- ||v1|| dan ||v2|| adalah panjang (magnitude) dari vektor A dan B secara berturut-turut.

## Data Understanding
  
  
