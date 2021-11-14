# -*- coding: utf-8 -*-
"""Submission1_PredictiveAnalytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aqU1igQM0aB4OzOPL-7iPenSQIPSr5Fq

**Biodata**
* Nama     : Rachel Gultom
* Email    : rachelgultom5@gmail.com
* Domisili : Asahan,Sumatera Utara
* Github (termasuk README.MD) : https://github.com/RachelGultom2000/Submission1_PredictiveAnalytics_MLTerapan
* Drive (Dataset) : https://drive.google.com/drive/folders/1w8KZ34YMEjLOuv6qs8ebfAA1XZ75kbpz?usp=sharing
Submission1_PredictiveAnalytics_MLTerapan
* Nama Tugas : Submission 1 - ML Terapan

## Prediksi Penyakit Stroke dengan Menggunakan Algoritma Logistic Regression ##

### Metode :
- Logistic Regression
- Random Forest

Import Library seperti Pandas,Scikit-learn,Searborn dan lainnya
"""

# Import Library

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import log_loss

import seaborn as sns

"""# Pre-Processing
## Beriku adalah langkah-langkah dalam melakukan preprocessing :
1. Melakukan load dataset ke dalam data frame
2. Memberikan tanda *numerical features* dari data dalam mempermudah proses scalling
3. Melakukan drop kolom untuk gender,ever_married,work_type,Residence_type dan smoking_status karena mesin tidak bisa membaca tipe data string (seharusnya bisa dengan convert,tetapi tidak disarankan karena berpotensi merusak akurasi data)
4. Mengisi missing value dengan nilai median.Missing value adalah kondisi dimana sebuah kolom tidak memiliki nilai atau NaN.Dengan median,data akan kembali di normalkan sehingga akan mempengarungi kebaikan dataset.
5. Melakukan pemisahan antara dataset train dan dataset test dengan proporsi pembagian :
  - 75% untuk data latih(train)
  - 25% untuk data uji(test)
6. Scalling dengan menggunakan Standard Scaler dari sklearn berfungsi agar fitur numerik dapat diproses lebih mudah oleh si mesin dalam proses modelling.

## Melakukan load dataset (memamasukkan dataset atau membaca) & Memberikan tanda pada num features.
Load dataset ke dalam dataframe
"""

# Menampilkan dataset

df = pd.read_csv('stroke_dataset.csv')
numerical_features = ['heart_disease','avg_glucose_level','bmi','age']
df

"""## Drop Column 
Melakukan drop terhadap kolom adalah salah satu cara yang baik agar model menjadi lebih baik karena terkadang si mesin tidak bisa membaca kolom yang bertipe data string.
"""

# Menghapus kolom dataset yang tidak diperlukan

df.drop(columns=['gender','ever_married', 'work_type', 'Residence_type','smoking_status'], inplace=True)
 
df

"""##  Mengecek Nilai NaN
Melakukan pengecekan terhadap setiap kolom untuk menemukan apakah ada yang mengandung missing value atau NaN
"""

# Mengecek apakah kolom mengandung missing value atau nilai NaN

for i in df.columns :
  print (i+": "+str(df[i].isna().sum()))

"""# Mengatasi Missing Value
Salah satu caranya adalah dengan mengisinya dengan nilai median(tengah).Missing Value akan membuat kolom tersebut tidak dapat diproses dan harus diisi jika ingin diproses.Pengisian data menggunakan nilai median akan membantu dalam menormalkan data yang hilang akibat kesalahan teknis dataset dan mempengarungi model tentunya.
"""

# Mengisi nilai atau data kosong pada dataset dengan median dari kolom.

df['hypertension'] = df['hypertension'].fillna(df['hypertension'].median())
df['heart_disease'] = df['heart_disease'].fillna(df['heart_disease'].median())
df['stroke'] = df['stroke'].fillna(df['stroke'].median())
df['bmi'] = df['bmi'].fillna(df['bmi'].median())
df['avg_glucose_level'] = df['avg_glucose_level'].fillna(df['avg_glucose_level'].median())
df['age'] = df['age'].fillna(df['age'].median())

"""## Melakukan Pengecekan Nilai NaN (2)
Melakukan pengecekan kembali apakah ada kolom yang mengandung nilai NaN atau tidak dengan tujuan agar proses selanjutnya bisa berjalan dengan baik
"""

# Memerika pada setiap kolom diatas untuk mencari nilai kosong atau missing value (NaN) setelah tahap pre-processing

for i in df.columns:
  print(i+" :" + str(df[i].isna().sum()))

"""Menampilkan data dari hasil pre-processing"""

# Tampilkan data hasil preprocessing
df.describe()

"""## Mendefinisikan X dan y
Ini merupakan salah satu tahap yang berhubungan dengan model.
- X adalah variabel yang menjadi tolak ukur untuk melakukan prediksi.
- y merupakan variabel yang menjadi tujuan dari hasil prediksinya

"""

# Definisikan variabel X dan y sebagai bahan melakukan prediksi

X = df.drop('stroke',axis='columns')
y = df['stroke']

"""## Split Train-Test dan Standard Scalling.

Memisah antara data train dan data test adalah bagian terpenting dari proses machine learning dimana ini bertujuan agar hasil akurasi dan model dapat diketahui.
Proporsi pembagiannya adalah
- 75% untuk data latih (train)
- 25% untuk data uji (test)

Dilanjutkan dengan melakukan standard scalling untuk data data numerik.
Scalling dilakukan dengan library Standard Scaller dari sklearn.Tujuannya agar fitur numerik dapat diproses lebih mudah pada tahap modelling.
"""

# Pemisahan Dataset dan Scalling terhadap variabel

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

# import StandardScaler
scaler = StandardScaler()

# fit dan transform untuk data trainning
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])

# transform untuk data testing
X_test[numerical_features] = scaler.transform(X_test.loc[:, numerical_features])

"""# Modelling (Pemilihan Algoritma)
Pembuatan model didasari oleh 2 algoritma yang dipilih,yaitu :

- Logistic Regression <br>
Digunakan untuk melakukan prediksi probabilitas kejadian suatu peristiwa dengan mencocokan datanya ke fungsi logit kurva logistik.

- Random Forest <br>
Merupakan salah satu metode dalam Decision Tree dimana pohon keputusan utuh terbentuk dari banyak decision tree atau estimators yang memberikan pendapat masing masing dengan bentuk pohon kecil.Random Forest memiliki ketergantungan terhadap Decision Tree.

Penggunaan Model <br>
Berdasarkan hasil tersebut,maka dapat dilihat bahwa akurasi model dari Logistic Regression jauh lebih tinggi atau melewati standard dibandingkan dengan algoritma Random Forest.Maka kesimpulannya,algoritma Logistic Regression menjadi pilihan yang tepat.
"""

# Mendefinisikan Model dan Metode yang akan dibentuk

logRes_model = LogisticRegression(max_iter=1000)
RF_model = RandomForestRegressor(n_estimators=1000,
            max_depth=16, random_state=55, n_jobs=1)

"""## Melakukan Trainning pada kedua algoritma atau metode.
Melakukan trainning atau fitting terhadap kedua algoritma menggunakan dataset yang sama yaitu data train dan menggunakan fit untuk sintaksnya
"""

# Melakukan fitting(latih) terhadap model menggunakan dataset train pada 2 model
# yaitu Logistic Regression dan Random Forest Regressor

logRes_model.fit(X_train,y_train)
RF_model.fit(X_train,y_train)

"""## Proses Testing Model
Melakukan testing pada data test dengan prediksi data yang ada pada dataset test lalu menampilkannya dalam bentuk akurasi.
"""

# Melakukan prediksi terhadap dataset test dan menampilkan hasilnya

logRes_y_pred = logRes_model.predict(X_test)
RF_y_pred = RF_model.predict(X_test)

print("Akurasi algoritma Logistic Regression : {}".format(logRes_model.score(X_test,y_test).round(3)))
print("Akurasi algoritma Random Forest : \t : {} ".format(RF_model.score(X_test,y_test).round(3)))

"""## Hasil Model Test
Berdasarkan hasil tersebut , maka dapat dilihat bahwa akurasi dari algoritma Logistic Regression memiliki akurasi yang jauh lebih tinggi dari Random Forest yaitu sebesar 0.937 atau 93%.

# Evaluasi
Dalam proses evaluasi, disajikan informasi mengenai algoritma yang dipilih yaitu Logistic Regression serta penjelesan mengenai perbandinganya dengan algoritma Random Forest,dalam kasus ini yaitu :
- Akurasi
- MSE (Mean Squared Error)

Penjelasan lebih lanjut mengenai algoritma yang dipilih ialah :
- Bobot dan nilai bias dari algoritma
- Visualisasi Heatmap dari Confussion Matrix

## Metrik #1 : Akurasi
Dari hasil yang didapatkan, akurasi yang dihasilkan Logistic Regression lebih tinggi dari Random Forest dan terlihat memiliki rentang nilai yang cukup jauh dimana Logistic Regression mencapai 0.937 sedangkan Random Forest hanya 0.039.
"""

# Metrik 1 : Akurasi, perbandingan kedua model diatas.

print("Akurasi algoritma Logistic Regression: {}".format(logRes_model.score(X_test,y_test).round(3)))
print("Akurasi algoritma Random Forest\t: {}".format(RF_model.score(X_test,y_test).round(3)))

"""## Metrik #2: MSE
Melakukan pengecekan dengan menggunakan MSE pada algoritma Linear Regression dan Random Forest. Dalam bagian ini disajikan sebuah grafik dari perbandingan kedua algoritma
"""

# Metrik 2 : MSE,mengecek Mean Squared Error(MSE) pada kedua model diatas.

mse = pd.DataFrame(columns=['train', 'test'], index=['LogRes','RF'])
dict_model = {'LogRes': logRes_model, 'RF': RF_model}
for name, model in dict_model.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3 
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3
mse

"""Menampilkan hasil plotting MSE dalam perbandingan kedua algoritma."""

# Tampilkan hasil plotting MSE

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""## Bobot dan nilai bias Logsitic Regression

Mencari bobot dari masing masing variabel yang ada dalam Linear Regression dengan tujuan untuk mengetahui nilai dari nilai bobot pada setiap variabel dan nilai bias dari setelah dilakukan sejumlah N perulangan
"""

# Mencari nilai bobot dari masing masing variabel yang terdapat dalam model

print("Nilai Bobot Tiap Variabel:\n{}\n\nNilai Bias: {}\n\nBanyaknya iterasi: {}".format(logRes_model.coef_[0], logRes_model.intercept_[0], logRes_model.n_iter_[0]))

"""## Confussion Matric Logistic Regression
Menciptakan confussion matrix untuk mengetahui letak prediksi yang salah maupun prediksi yang benar pada saat mesin sedang melakukan proses prediksi.
"""

# Membuat Confussion Matrix agar dapat mencari kesalahan dalam prediksi model (akurasi)

logRes_cn = confusion_matrix(y_test,logRes_y_pred)
print("Confusion Matrix Logistic Regression: \n{}".format(logRes_cn))

"""## Heatmap Visualisasi Confussion Matrix
Visualisasi data melalui heatmap bertujuan untuk melihat lebih jelas distribuasi dari hasil model.
"""

# Heatmap menggunakan SNS

sns.heatmap(logRes_cn, annot=True)