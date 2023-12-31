# -*- coding: utf-8 -*-
"""MLT2 fix2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11QSEWTSWiILF1rCuPruhFSYdu0I2z-mK

<h1><strong>Sistem Rekomendasi: Rekomendasi Kursus Online pada Udemy Courses<strong><h1>
Nama : Ayudha Kusuma R.
Machine Learning Terapan - Dicoding

link dataset :  https://www.kaggle.com/datasets/andrewmvd/udemy-courses

# 1.Melakukan Import Modul yang diperlukan
"""

# Memasang modul plotly, scikit-learn, & neattext terbaru
!pip install -q -U plotly
!pip install -q -U scikit-learn
!pip install -q -U neattext

# Untuk pengolahan data
import numpy as np
import pandas as pd
import neattext.functions as nfx
import matplotlib.pyplot as plt
import seaborn as sns

# Untuk visualisasi data
import missingno as msno
import plotly.express as px
from plotly.offline import iplot



# Untuk pembuatan sistem rekomendasi
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""# 2.Melakukan Persiapan Dataset"""

# Membuat folder .kaggle di dalam folder root, kemudian menyalin berkas kaggle.json pada direktori aktif saat ini ke folder .kaggle
!chmod 600 kaggle.json && (ls ~/.kaggle 2>/dev/null || mkdir ~/.kaggle) && mv kaggle.json ~/.kaggle/

# Mengunduh dataset menggunakan Kaggle CLI
!kaggle datasets download -d thedevastator/udemy-courses-revenue-generation-and-course-anal

# Mengekstrak berkas zip ke direktori aktif saat ini dan menghapus file zip
!unzip -q /content/udemy-courses.zip && rm udemy-courses.zip

"""# 3.Pemahaman Data (Data Understanding)"""

# Memuat data pada dataframe
raw_df = pd.read_csv('/content/udemy_courses.csv')

# Melakukan Pratinjau dataset
raw_df.head()

# Memuat informasi dataframe
raw_df.info()

# Menghitung jumlah data kosong pada setiap kolom
raw_df.isna().sum()

sorted_null = msno.nullity_sort(raw_df, sort='ascending')
figures = msno.matrix(sorted_null, color=(1, 0.43, 0.43))

raw_df.corr()

"""# 4.Persiapan Data (Data Preparation) dan Visualisasi Data"""

# Melihat jumlah data duplikasi
raw_df.duplicated().sum()

# Menghapus data duplikasi
raw_df.drop_duplicates(inplace=True)

# Melihat informasi dataframe
raw_df.info()

# Hasil data setelah dibersihkan
raw_df.head(5)

"""## 4.1 Cleaning data duplicate"""

# Melihat jumlah data duplikasi
raw_df.duplicated().sum()

# Menghapus data duplikasi
raw_df.drop_duplicates(inplace=True)
# Melihat informasi dataframe
raw_df.info()

# Hasil data setelah dibersihkan
raw_df.head(5)

"""## 4.2 Visualisasi data"""

# Fungsi untuk plot distribusi data pada suatu kolom numerik
def plot_distribution(column:str, title:str):
  figures = px.histogram(data_frame=raw_df,
                        x=column,
                        color='is_paid',
                        template='plotly_white',
                        marginal='box',
                        color_discrete_sequence=["#78C1F3","#9BE8D8"],
                        barmode='overlay',
                        histfunc='count')

  figures.update_layout(font_family='Open Sans',
                        title=dict(text=title,
                                  x=0.5,
                                  font=dict(color="#333",size=20)),
                        hoverlabel=dict(bgcolor='white'))

  figures.update_xaxes(
      automargin=True
  )

  iplot(figures)

# Fungsi untuk plot bar data pada suatu kolom numerik
def plot_bar(column:str, title:str):
  figures = px.bar(data_frame=raw_df,
                  x="subject",
                  y=column,
                  color="is_paid",
                  barmode="group",
                  template='plotly_white',
                  color_discrete_sequence=["#78C1F3","#9BE8D8"])

  figures.update_layout(font_family='Open Sans',
                        title=dict(text=title,
                                  x=0.5,
                                  font=dict(color="#333",size=20)),
                        hoverlabel=dict(bgcolor='white'))

  figures.update_xaxes(
      automargin=True
  )

  iplot(figures)

# Fungsi untuk plot pie data pada suatu kolom kategori
def plot_category(column:str, title:str):
  figures = px.sunburst(raw_df,
                      path=["is_paid",column],
                      color="num_subscribers",
                      color_continuous_scale=["#78C1F3","#9BE8D8"])

  figures.update_layout(font_family='Open Sans',
                        title=dict(text=title,
                                   x=0.5,
                                   font=dict(color="#333",size=20)),
                        title_y=0.96)

  figures.update_traces(hovertemplate="Labels = %{label}<br>Count = %{value}<br>Subscribers = %{color:.0f} <extra></extra>")

  figures.update_xaxes(
      automargin=True
  )

  iplot(figures)

# Menampilkan visualisasi data penerapan fitur numerik
for column in ['price', 'num_subscribers', 'num_reviews', 'num_lectures', 'content_duration']:
  plot_distribution(column=column, title=f"Distribusi fitur numerik pada kolom {column}")

# Menampilkan visualisasi data
for column in ['price', 'num_subscribers', 'num_reviews', 'num_lectures', 'content_duration']:
  plot_bar(column=column, title=f"Distribusi label {column} dengan label subjek<br>Berdasarkan tipe kursus")

# Menampilkan visualisasi data fitur kategori
for column in [ 'level', 'subject']:
  plot_category(column=column, title=f"Distribusi label {column} dan tipe kursus<br>Berdasarkan jumlah subscriber")

"""## 4.3 Seleksi dan Pembersihan data yang digunakan sebagai fitur"""

# Memberi nama ulang kolom course_title yang berlum diproses
raw_df['raw_course_title'] = raw_df['course_title']

# Menghilangkan stopword pada course_title
raw_df['course_title'] = raw_df['raw_course_title'].apply(nfx.remove_stopwords)

# Menghapus karakter spesial pada course_title
raw_df['course_title'] = raw_df['course_title'].apply(nfx.remove_special_characters)

# Melihat perbandingan course_title yang telah dibersihkan
raw_df[['course_title', 'raw_course_title']]

"""## 4.4 Rekayasa Fitur dengan TF-IDF Vectorizer"""

# Menyimpan indeks kursus
course_indices = pd.Series(raw_df.index,index=raw_df['course_title']).drop_duplicates()
course_indices.head()

# Menyimpan nama-nama kursus pada dataframe baru
df_course = pd.DataFrame({'course_title':raw_df['course_title']})

# Pratinjau data
df_course.head()

# Inisialisasi TfidfVectorizer
vect = TfidfVectorizer()

# Vektorisasi teks
tfidf_matrix = vect.fit_transform(raw_df['course_title'])

# Ubah vektor ke dataframe
df = pd.DataFrame(tfidf_matrix.todense(), columns=vect.get_feature_names_out())

# Pratinjau data
df.head()

"""# 5.Pembuatan Sistem Rekomendasi Content-Based Filtering

## 5.1 Dengan model K-Nearest Neighbor
"""

# Membuat sistem rekomendasi dengan model K-Nearest Neighbor
# Inisiasi model
model = NearestNeighbors(metric='euclidean')

# Melakukan fitting model terhadap data
model.fit(df)

# Membuat fungsi untuk mendapatkan rekomendasi
# Dengan model KNN
def getRecommendedCourses_model(course_title:str, recommend_courses:int=10):
  idx = course_indices[course_title]
  print(f'Apabila pengguna menyukai course {course_title[0]}\n{recommend_courses} course berikut ini juga mungkin akan disukai :')
  # Mencari course terdekat dengan course yang diikuti pengguna
  distances, neighbors = model.kneighbors(df.loc[idx],n_neighbors=recommend_courses)
  # Memasukkan course yang sama pada sebuah list
  similar_courses = []
  for course in df_course.loc[neighbors[0][:]].values:
    similar_courses.append(course[0])
  # Memasukan skornya (jarak) pada sebuah list
  similar_distance = []
  for distance in distances[0]:
    similar_distance.append(f"{round(100-distance, 2)}%")
  # Mengembalikan sebuah dataframe berupa rekomendasi berdasarkan judul course
  return pd.DataFrame(data = {"Judul Kursus" : similar_courses, "Tingkat Kesamaan" : similar_distance})

# Memberikan rekomendasi terhadap course yang
# Serupa dengan Succeed Forex Know Start
getRecommendedCourses_model(df_course.loc[500])

# data_ke_500 = df.loc[500, ['course_title','subject']]
# data_ke_500 = pd.DataFrame(data_ke_500).transpose()
# data_ke_500.columns = ['course_title','subject']
# data_ke_500

"""## 5.2 Dengan Cosine Similarity"""

# Menghitung cosine similarity dari dataframe
cosine_sim = cosine_similarity(df)

# Menyimpan hasil perhitungan pada dataframe
cosine_sim_df = pd.DataFrame(cosine_sim, index=df_course['course_title'], columns=df_course['course_title'])
cosine_sim_df.head(3)

# Membuat fungsi untuk mendapatkan rekomendasi
# Dengan Cosine Similarity
def getRecommendedCourses_cosine(course_title:str, recommended_courses:int=10):
  print(f'Apabila pengguna menyukai course {course_title[0]}\n{recommended_courses} course berikut ini juga mungkin akan disukai :')
  # Mencari nilai unik pada course yang dimainkan pengguna di baris dataframe cosine sim
  # Nilai unik (arr) dikembalikan dalam bentuk yang berurutan dari kecil ke besar
  arr, ind = np.unique(cosine_sim_df.loc[course_title[0]], return_index=True)
  # Memasukkan nama course yang serupa dari index kedua terakhir sampai index n terakhir
  similar_course = []
  for index in ind[-(recommended_courses+1):-1]:
    similar_course.append(df_course.loc[index][0])
  # Memasukkan skor cosine dari course yang serupa mulai dari index kedua terakhir sampai index n terakhir
  cosine_score = []
  for score in arr[-(recommended_courses+1):-1]:
    cosine_score.append(score)
  # Mengembalikan sebuah dataframe berupa rekomendasi berdasarkan judul course
  return pd.DataFrame(data = {"Judul Kursus" : similar_course, "Cosine Similarity" : cosine_score}).sort_values(by='Cosine Similarity',ascending=False).reset_index(drop=True)

# Memberikan rekomendasi terhadap course yang
# Serupa dengan Succeed Forex Know Start
getRecommendedCourses_cosine(df_course.loc[500])

"""# 6. Evaluasi"""

# Fungsi untuk menghitung nilai presisi dari sistem rekomendasi
def precision(query:pd.DataFrame, rec_result:pd.DataFrame):
  relevant = 0
  for result in rec_result['subject'].values.tolist():
    if query['subject'].values == result:
      relevant += 1
  #return relevant/len(rec_result)
  return relevant



# Query input untuk evaluasi
query_input = raw_df.loc[raw_df['course_title'].isin(df_course.loc[500].values.tolist())][['course_title', 'subject']]
query_input

# Memberikan rekomendasi terhadap course yang
# Serupa dengan Succeed Forex Know Start
# Dengan model KNN
knn_result_df = getRecommendedCourses_model(df_course.loc[500])
knn_result_df

# Menyimpan course_title dan subject untuk proses evaluasi
knn_result = raw_df.loc[raw_df['course_title'].isin(knn_result_df['Judul Kursus'].values.tolist())][['course_title', 'subject']].iloc[:10]
knn_result

# Memberikan rekomendasi terhadap course yang
# Serupa dengan Succeed Forex Know Start
# Dengan Cosine Similarity
cosine_result_df = getRecommendedCourses_cosine(df_course.loc[500])
cosine_result_df

# Menyimpan course_title dan subject untuk proses evaluasi
cosine_result= raw_df.loc[raw_df['course_title'].isin(cosine_result_df['Judul Kursus'].values.tolist())][['course_title', 'subject']]
cosine_result

# Perhitungan precision
print(f"Nilai precision menggunakan Cosine Similarity adalah {precision(query_input, cosine_result)}")

print(cosine_result)

len(cosine_result)

print(cosine_result)

print(query_input)

# Perhitungan precision model KNN
print(f"Nilai precision menggunakan K-Nearest Neighbor adalah {precision(query_input, knn_result)}")

len(knn_result)

print(knn_result_new)

"""# Penutupan

Model untuk memberikan rekomendasi kursus online untuk pengguna di Udemy telah selesai dibuat. Setelah diujikan, model ini bekerja cukup baik dalam memberikan  rekomendasi teratas terhadap kursus yang diikuti pengguna. Namun, masih ada beberapa kekurangan dari model yang dibuat seperti yang terlihat pada skor Precision. Untuk memperbaikinya dapat digunakan algoritma untuk membuat model rekomendasi yang lain seperti menggunakan _deep learning_ lalu dibandingkan performanya dengan model KNN saat ini.


### Referensi
* Dokumentasi Scikit-learn: https://scikit-learn.org/stable/
* Dokumentasi Plotly: https://plotly.com/python/
* Dokumentasi Neat Text: https://blog.jcharistech.com/neattext/
* Lainnya:
  * https://www.kaggle.com/andrewmvd/udemy-courses
  * https://www.kaggle.com/kaanboke/plotly-beginner-friendly-udemy
  * https://www.kaggle.com/shirishsharma/analysis-of-data-with-plotly-and-ml-models



"""