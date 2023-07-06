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
  
  <img width="743" alt="udemy" src="https://github.com/yudhakr/MLT2/assets/84507343/e29dec4a-5007-4d8e-b58d-c98bca67f223">


  Tabel di bawah ini merupakan informasi dari dataset yang digunakan:

| Jenis                   | Keterangan                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------ |
| Sumber                  | [Kaggle Dataset: Udemy Courses](https://www.kaggle.com/andrewmvd/udemy-courses)                  |
| Lisensi                 | License was not specified at source                                                              |
| Kategori                | Bisnis, Edukasi, Komunitas Online                                                                |
| Rating Penggunaan       | 10.0 (Gold)                                                                                      |
| Jenis dan Ukuran Berkas | zip (694 kB)                                                                                     |


Gambar di bawah ini merupakan sampel dari dataset pada berkas `udemy_courses.csv`:

|   |   | course_id |                                      course_title |                                               url | is_paid | price | num_subscribers | num_reviews | num_lectures |              level | content_duration |  published_timestamp |          subject |
|---|--:|----------:|--------------------------------------------------:|--------------------------------------------------:|--------:|------:|----------------:|------------:|-------------:|-------------------:|-----------------:|---------------------:|-----------------:|
|   | 0 |   1070968 |                Ultimate Investment Banking Course | https://www.udemy.com/ultimate-investment-bank... |    True |   200 |            2147 |          23 |           51 |         All Levels |              1.5 | 2017-01-18T20:58:58Z | Business Finance |
|   | 1 |   1113822 | Complete GST Course & Certification - Grow You... |     https://www.udemy.com/goods-and-services-tax/ |    True |    75 |            2792 |         923 |          274 |         All Levels |             39.0 | 2017-03-09T16:34:20Z | Business Finance |
|   | 2 |   1006314 | Financial Modeling for Business Analysts and C... | https://www.udemy.com/financial-modeling-for-b... |    True |    45 |            2174 |          74 |           51 | Intermediate Level |              2.5 | 2016-12-19T19:26:30Z | Business Finance |
|   | 3 |   1210588 | Beginner to Pro - Financial Analysis in Excel ... | https://www.udemy.com/complete-excel-finance-c... |    True |    95 |            2451 |          11 |           36 |         All Levels |              3.0 | 2017-05-30T20:07:24Z | Business Finance |
|   | 4 |   1011058 |      How To Maximize Your Profits Trading Options | https://www.udemy.com/how-to-maximize-your-pro... |    True |   200 |            1276 |          45 |           26 | Intermediate Level |              2.0 | 2016-12-13T14:57:18Z | Business Finance |



Kemudian informasi type dataset pada berkas

<img width="277" alt="2" src="https://github.com/yudhakr/MLT2/assets/84507343/3c13bdbc-f991-42f2-bdff-0ef3875f8785">

Berkas udemy_courses.csv berisi informasi lengkap tentang kursus-kursus online yang tersedia di platform Udemy. Dataset ini sangat terorganisir, tidak ada nilai yang kosong, dan mengandung kolom-kolom berikut dengan penjelasan masing-masing:

1. Kolom course_id berisi ID unik untuk setiap kursus dalam dataset.
1. Kolom course_title berisi judul dari setiap kursus.
1. Kolom url berisi URL yang mengarah ke kursus tersebut.
1. Kolom is_paid berisi informasi apakah kursus tersebut berbayar atau gratis, dengan tipe data boolean.
1. Kolom price berisi harga kursus dalam mata uang dolar.
1. Kolom num_subscribers berisi jumlah pengguna yang berlangganan pada kursus tersebut.
1. Kolom num_reviews berisi jumlah ulasan yang diberikan oleh pengguna yang berlangganan pada kursus tersebut.
1. Kolom num_lectures berisi jumlah pengajar atau materi yang ada dalam kursus tersebut.
1. Kolom level berisi tingkat kesulitan dari kursus, seperti "Pemula", "Menengah", atau "Mahir".
1. Kolom content_duration berisi durasi total konten dalam kursus tersebut.
1. Kolom published_timestamp berisi waktu publikasi atau tanggal kursus tersebut diterbitkan.
1. Kolom subject berisi subjek atau topik yang diajarkan dalam kursus tersebut.
Dataset ini menyediakan informasi penting tentang setiap kursus online, sehingga dapat digunakan untuk analisis, evaluasi, atau pengembangan sistem rekomendasi dalam konteks pembelajaran online.

Beberapa Visualisasi dari dataset yang digunakan :
- Visualisasi dengan Data Numerik
  <img width="883" alt="visual 1" src="https://github.com/yudhakr/MLT2/assets/84507343/4640a0a5-0c03-4248-85ba-5d671c50337e">
  
__Gambar 1__ : Merupakan visualisasi Penerapan Distribusi pada kolom price (Harga)
  
<img width="888" alt="visual 2" src="https://github.com/yudhakr/MLT2/assets/84507343/886e49ea-1b87-47ac-9a7f-7546f8814846">

__Gambar 2__ : Merupakan numerik pada kolom  (Jumlah Berlangganan)

<img width="842" alt="6" src="https://github.com/yudhakr/MLT2/assets/84507343/60cebdbd-dc7e-4e8d-8d90-51758997ba1c">

__Gambar 3__ : Menjelaskan Distribusi label price dengan label subjek berdasarkan tipe kursus seperti Business Finance,Graphic Design, Musical Instruments, dan Web Development.

- Visualisasi dengan Data Kategori
  
<img width="592" alt="10" src="https://github.com/yudhakr/MLT2/assets/84507343/8e584b8c-9de4-41f4-b095-c6bcf5ef6e6a">
 
  __Gambar 4__ : Kategori Level Kelas dengan banyaknya juamlah yang berlangganan (Subscribe)

  
Seperti yang sudah dijelaskan pada bagian _Solution approach_, berikut adalah tahapan-tahapan dalam melakukan pra-pemrosesan data:
- Membersihkan data duplikasi. Hal ini dilakukan karena data duplikat dapat menyebabkan munculnya redundansi dalam hasil sistem rekomendasi yang akan dibuat. Oleh karena itu data duplikasi ini perlu dihilangkan karena data tersebut sudah terdapat dalam dataset. Proses ini dilakukan dengan menggunakan fungsi `drop_duplicates` dari _dataframe_ dataset.
- Membersihkan teks judul pada kolom `course_title` dari `stopwords`. Hal ini dilakukan untuk mencegah redundansi pada data teks judul dengan cara menghapus informasi tingkat rendah sehingga sistem rekomendasi nantinya dapat fokus pada informasi yang lebih penting. Selain itu, menghapus `stopwords` dapat mengurangi ukuran dataset. Proses ini dilakukan dengan menggunakan fungsi `remove_stopwords` pada modul [neattext](https://blog.jcharistech.com/neattext/).
- Membersihkan teks judul pada kolom course_title dari karakter spesial. Hal ini dilakukan untuk mencegah kebingungan sistem rekomendasi dengan cara menghapus karakter khusus yang memiliki informasi rendah. Proses ini dilakukan dengan menggunakan fungsi `remove_special_characters` pada modul [neattext](https://blog.jcharistech.com/neattext/).
- Konversi teks judul yang telah dibersihkan menjadi vektor TF-IDF. Hal ini dilakukan untuk melakukan ekstraksi fitur pada teks judul kursus yang nantinya akan dikonversi menjadi vektor dengan nilai numerik. Proses ini dilakukan dengan menggunakan fungsi [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) pada modul scikit-learn. Proses perhitungannya yaitu:
  - Menghitung nilai _Term Frequency_ dari sebuah kata atau kalimat dalam dokumen. Salah satu cara yang paling sederhana adalah menghitung jumlah awal kata/kalimat yang muncul dalam dokumen kemudian menyesuaikan frekuensi berdasarkan panjang dokumen. Secara matematis, nilainya akan dihitung dengan rumus berikut:
  
     $$tf(t,d) = log(1 + freg(t,d)) $$

  - Menghitung nilai _Inverse Document Frequency_ dari sebuah kata/kalimat dalam satu set dokumen. Semakin dekat nilainya ke 0 maka semakin umum sebuah kata/kalimat. Metrik ini dirumuskan sebagai berikut:
    
    $$tf(t,D) = log(N / count(d ϵ D:t ϵ d) $$

  - Menghitung nilai TF-IDF. Hal ini dilakukan dengan cara mengalikan nilai TF dengan nilai IDF untuk menentukan seberapa relevan kata/kalimat tersebut dalam suatu dokumen. Secara matematis dirumuskan sebagai berikut:
    
    $$tf idf(t,d,D) = tf(t,d).idf(t,D) $$





